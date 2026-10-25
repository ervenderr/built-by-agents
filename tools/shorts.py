#!/usr/bin/env python3
"""Narration + audio verification for the channel's videos.

  shorts.py narrate script.txt OUT_DIR [--voice af_heart] [--speed 1.0]
      one sentence per line -> OUT_DIR/s01.wav ... -> OUT_DIR/narration.wav + timings.json.
      Each sentence is transcribed and must match its line, or the run fails.
  shorts.py verify video.mp4 script.txt
      transcribes the rendered audio and fails if it differs from the script.
  shorts.py selftest
"""
import argparse
import fcntl
import time
import difflib
import json
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
SENTENCE_MIN = 0.85   # shortcut: per-sentence ratio, tune if whisper mishears a brand name
FULL_MIN = 0.93       # whole-video ratio; the known "sentence one repeated, last dropped" bug scored ~0.83
GAP_S = 0.25
LOCK_FILE = "/tmp/youtube-os-voicestudio.lock"   # shortcut: fixed path, fine for one user on one machine
VOICESTUDIO = "http://localhost:3900"   # local, loopback-only API of the VoiceStudio app
SEED = "42"   # fixed seed = same voice character for every sentence and every video
NUM = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
       "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten"}


ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()


def spoken(n: int) -> str:
    """Whole number in words ("13,002" -> "thirteen thousand two"); whisper prints digits where the narrator said words."""
    if n < 20:
        return ONES[n]
    if n < 100:
        return TENS[n // 10] + (" " + ONES[n % 10] if n % 10 else "")
    for size, name in ((10**9, "billion"), (10**6, "million"), (1000, "thousand"), (100, "hundred")):
        if n >= size:
            return spoken(n // size) + " " + name + (" " + spoken(n % size) if n % size else "")


HOMOPHONE = {"wait": "weight", "waits": "weights"}   # whisper confuses them; both sides are normalized, so matching only gets looser for these


def words(text: str, join_hyphens: bool = True) -> list[str]:
    t = re.sub(r"\bchat gpt\b", "chatgpt", text.lower().replace("'", "").replace("\u2019", ""))   # whisper splits brand names; "weight's" ~ "weights"
    t = re.sub(r"\d{1,3}(?:,\d{3})+|\d+", lambda m: " " + spoken(int(m.group().replace(",", ""))) + " ", t)
    toks = re.sub(r"[^a-z0-9 ]", " ", t.replace("-", "" if join_hyphens else " ")).split()
    return [HOMOPHONE.get(NUM.get(x, x), NUM.get(x, x)) for x in toks]


def ratio(a: str, b: str) -> float:
    # whisper may drop or keep hyphens ("fixed-size" vs "fixed size", "non-linearity" vs "nonlinearity"): take the better reading
    return max(difflib.SequenceMatcher(None, words(a, j), words(b, j)).ratio() for j in (True, False))


def tail_ok(script: str, heard: str, n: int = 3) -> bool:
    return any(words(heard, j)[-n:] == words(script, j)[-n:] for j in (True, False))


def run(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode:
        sys.exit(f"command failed: {' '.join(cmd[:3])}...\n{r.stderr[-400:]}")
    return r


def transcribe(wav: Path) -> str:
    with tempfile.TemporaryDirectory() as td:
        out = run(["npx", "hyperframes", "transcribe", str(wav.resolve()), "--model", "small.en", "--json"], cwd=td).stdout
        path = json.loads(out[out.index("{"):])["transcriptPath"]   # the CLI says where it wrote the transcript
        data = json.loads(Path(path).read_text())
    ws = data if isinstance(data, list) else data.get("words", [])
    return " ".join(w["text"] for w in ws)


def duration(path: Path) -> float:
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                      "-of", "csv=p=0", str(path)]).stdout.strip())


def profile_id(name: str) -> str:
    with urllib.request.urlopen(f"{VOICESTUDIO}/profiles", timeout=20) as r:
        for p in json.load(r):
            if name in (p["name"], p["id"]):
                return p["id"]
    sys.exit(f"VoiceStudio profile not found: {name}")


def multipart(fields: dict[str, str]) -> tuple[bytes, str]:
    b = "----shorts" + "x" * 12
    body = b"".join(f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode()
                    for k, v in fields.items()) + f"--{b}--\r\n".encode()
    return body, f"multipart/form-data; boundary={b}"


def speak_voicestudio(text: str, wav: Path, voice: str, speed: str) -> None:
    body, ctype = multipart({"text": text, "profile_id": profile_id(voice), "seed": SEED,
                             "language": "English", "speed": speed})
    req = urllib.request.Request(f"{VOICESTUDIO}/generate", data=body, headers={"Content-Type": ctype})
    # one call at a time across all processes (parallel agents got HTTP 429), plus backoff on 429/503
    with open(LOCK_FILE, "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        for attempt in range(8):
            try:
                with urllib.request.urlopen(req, timeout=180) as r:
                    wav.write_bytes(r.read())
                return
            except urllib.error.HTTPError as e:
                if e.code not in (429, 503) or attempt == 7:
                    sys.exit(f"VoiceStudio API HTTP {e.code}: {e.read()[:200]!r}")
                time.sleep(min(2 ** attempt, 30))
            except OSError as e:
                sys.exit(f"VoiceStudio API call failed (is the app running on :3900?): {e}")


FIT_MIN, FIT_MAX = 0.75, 1.33   # shortcut: tempo change limit when fitting to old scene timings


def narrate(script: Path, out: Path, voice: str, speed: str, engine: str = "kokoro",
            fit: Path | None = None) -> None:
    lines = [l.strip() for l in script.read_text().splitlines() if l.strip()]
    if not lines:
        sys.exit("script is empty")
    out.mkdir(parents=True, exist_ok=True)
    old = json.loads(fit.read_text()) if fit else None
    if old and len(old) != len(lines):
        sys.exit(f"--fit timings have {len(old)} sentences, script has {len(lines)}")
    parts, timings, t = [], [], 0.0
    for i, line in enumerate(lines, 1):   # sequential on purpose; parallel/array-indexing bugs broke two videos
        wav = out / f"s{i:02d}.wav"
        if engine == "voicestudio":
            speak_voicestudio(line, wav, voice, speed)
        else:
            run([str(HERE / "narrate.sh"), line, str(wav), voice, speed])
        heard = transcribe(wav)
        r = ratio(line, heard)
        if r < SENTENCE_MIN:
            sys.exit(f"sentence {i} mismatch (ratio {r:.2f})\n  wanted: {line}\n  heard:  {heard}")
        d = duration(wav)
        if old:   # stretch/squeeze this sentence into its existing scene slot so no animation needs retiming
            slot = old[i - 1]["duration"]
            r = d / slot
            if not FIT_MIN <= r <= FIT_MAX:
                sys.exit(f"sentence {i} would need tempo x{r:.2f} to fit its slot; retime the scenes instead")
            fitted = out / f"s{i:02d}.fit.wav"
            run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(wav), "-af", f"atempo={r:.4f},apad=whole_dur={slot}",
                 "-t", str(slot), str(fitted)])
            wav, d = fitted, slot
        timings.append({"i": i, "text": line, "start": round(old[i - 1]["start"] if old else t, 3),
                        "duration": round(d, 3)})
        parts.append(wav)
        t = timings[-1]["start"] + d + (0 if old else GAP_S)
    lst = out / "list.txt"
    seq = []
    for k, p in enumerate(parts):
        seq.append(f"file '{p.resolve()}'")
        if k < len(parts) - 1:
            gap = timings[k + 1]["start"] - (timings[k]["start"] + timings[k]["duration"]) if old else GAP_S
            sil = out / f"gap{k}.wav"
            run(["ffmpeg", "-loglevel", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
                 "-t", f"{max(gap, 0.01):.3f}", str(sil)])
            seq.append(f"file '{sil.resolve()}'")
    lst.write_text("\n".join(seq) + "\n")
    run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
         "-ar", "24000", "-ac", "1", str(out / "narration.wav")])
    (out / "timings.json").write_text(json.dumps(timings, indent=2))
    print(f"ok: {len(lines)} sentences, {t - GAP_S:.2f}s -> {out}/narration.wav, timings.json")


def verify(video: Path, script: Path) -> None:
    want = " ".join(l.strip() for l in script.read_text().splitlines() if l.strip())
    with tempfile.TemporaryDirectory() as td:
        wav = Path(td) / "a.wav"
        run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(video), "-vn", "-ac", "1", "-ar", "16000", str(wav)])
        heard = transcribe(wav)
    r = ratio(want, heard)
    ok = r >= FULL_MIN and tail_ok(want, heard)
    print(f"{'PASS' if ok else 'FAIL'} ratio={r:.2f} tail_ok={tail_ok(want, heard)}\n  heard: {heard}")
    sys.exit(0 if ok else 1)


def selftest() -> None:
    s = ("Recursion is a function solving a problem by calling itself. Each call gets a smaller version of the "
         "problem. Without a base case to stop, it never ends. Factorial of three waits for two, which waits for one. "
         "Then the answers come back up: six. Still confused? See: recursion.")
    bad = ("Recursion is a function, solving a problem by calling itself. Recursion is a function, solving a problem "
           "by calling itself. Each call gets a smaller version of the problem. Without a base case to stop, it never "
           "ends. Factorial of three waits for two, which waits for one. Then the answers come back up, six.")
    good = ("Recursion is a function, solving a problem by calling itself. Each call gets a smaller version of the "
            "problem. Without a base case to stop, it never ends. Factorial of 3 waits for 2, which waits for 1. "
            "Then the answers come back up. 6. Still confused, see recursion.")
    assert words("the weight's caused it") == words("the weights caused it")
    assert words("weight by weight") == words("wait by wait")
    assert words("13,002 weights and 3 layers") == "thirteen thousand two weights and three layers".split()
    assert ratio(s, good) >= FULL_MIN and tail_ok(s, good), ratio(s, good)
    assert not (ratio(s, bad) >= FULL_MIN and tail_ok(s, bad)), ratio(s, bad)
    print("selftest ok", round(ratio(s, good), 2), round(ratio(s, bad), 2))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    n = sub.add_parser("narrate"); n.add_argument("script", type=Path); n.add_argument("out", type=Path)
    n.add_argument("--voice", default="af_heart"); n.add_argument("--speed", default="1.0")
    n.add_argument("--engine", choices=["kokoro", "voicestudio"], default="kokoro")
    n.add_argument("--fit", type=Path, help="previous timings.json: fit each sentence into its old slot")
    v = sub.add_parser("verify"); v.add_argument("video", type=Path); v.add_argument("script", type=Path)
    sub.add_parser("selftest")
    a = ap.parse_args()
    {"narrate": lambda: narrate(a.script, a.out, a.voice, a.speed, a.engine, a.fit),
     "verify": lambda: verify(a.video, a.script),
     "selftest": selftest}[a.cmd]()

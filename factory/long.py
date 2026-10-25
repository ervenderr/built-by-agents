#!/usr/bin/env python3
"""Long-form (16:9, ~5-15 min) factory: outline > script > facts > voice > build (chapters in parallel + stitch) > verify > meta > review.

  long.py run --topic "slug:angle" [--minutes 5] [--chapters 5]
Reuses factory.py (claude -p wrapper, live view, state) and tools/shorts.py (narrate, verify). Review/upload: factory/run.sh review
(upload.py sets the thumbnail and keeps the video private + scheduled).
"""
import argparse
import json
import re
import shutil
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

import factory as F
from rich.live import Live

STAGES = ["outline", "script", "facts", "voice", "build", "verify", "meta", "review"]
BUDGET = {"outline": 2.5, "script": 4.0, "facts": 4.0, "chapter": 6.0, "stitch": 8.0, "meta": 2.0}
GAP_S = 0.6   # silence between chapters
WPM = 150
F.STAGES[:] = STAGES
F.WORK[:] = STAGES[:-1]
F.AGENT.update({"outline": "outliner", "script": "script-writer", "facts": "fact-checker", "build": "chapter-builders + stitch"})


def chapters(d: Path) -> list[dict]:
    return json.loads((d / "outline.json").read_text())["chapters"]


def newest(paths: list[Path]) -> float:
    return max((p.stat().st_mtime for p in paths if p.exists()), default=0)


def done(slug: str, stage: str) -> bool:
    d = F.VIDEOS / slug
    sc, nar, mp4 = d / "script.txt", d / "assets/narration.wav", d / f"out/{slug}.mp4"
    facts = json.loads((d / "facts.json").read_text()) if (d / "facts.json").exists() else {}
    return {"outline": (d / "outline.json").exists(),
            "script": sc.exists() and (d / "SOURCES.md").exists(),
            "facts": bool(facts.get("ok")) and F.fresh(d / "facts.json", sc),
            "voice": F.fresh(nar, sc) and (d / "chapters.json").exists(),
            "build": F.fresh(mp4, nar),
            "verify": F.fresh(d / ".verified", mp4),
            "meta": (d / "metadata.json").exists() and (d / "thumbnail.png").exists()}.get(stage, False)


def write_script(d: Path, target_words: int) -> None:
    files = sorted((d / "script").glob("ch*.txt"))
    if len(files) != len(chapters(d)):
        raise F.StageError(f"script has {len(files)} chapter files, outline has {len(chapters(d))}")
    lines = [l.strip() for f in files for l in f.read_text().splitlines() if l.strip()]
    words = sum(len(l.split()) for l in lines)
    if not 0.7 * target_words <= words <= 1.3 * target_words:
        raise F.StageError(f"script has {words} words, target {target_words}")
    (d / "script.txt").write_text("\n".join(lines) + "\n")


def narrate_chapters(slug: str) -> None:
    d = F.VIDEOS / slug
    info, parts, full, t = [], [], [], 0.0
    for c in chapters(d):
        src, out = d / f"script/{c['id']}.txt", d / f"assets-vs/{c['id']}"
        if not F.fresh(out / "narration.wav", src):
            F.setst(slug, "voice", "run", f"narrating {c['id']}")
            r = F.tool("tools/shorts.py", "narrate", str(src), str(out), "--engine", "voicestudio", "--voice", "BuiltByAgentsExplainer")
            if r.returncode:
                raise F.StageError(f"voice {c['id']}: " + (r.stdout + r.stderr)[-200:])
        tim = json.loads((out / "timings.json").read_text())
        dur = tim[-1]["start"] + tim[-1]["duration"]
        (d / "chapters").mkdir(exist_ok=True)
        (d / f"chapters/{c['id']}.timings.json").write_text(json.dumps(tim, indent=2))
        info.append({"id": c["id"], "title": c["title"], "start": round(t, 3), "duration": round(dur, 3)})
        full += [{**x, "chapter": c["id"], "start": round(x["start"] + t, 3)} for x in tim]
        parts.append(out / "narration.wav")
        t += dur + GAP_S
    seq = []
    for k, p in enumerate(parts):
        seq.append(f"file '{p.resolve()}'")
        if k < len(parts) - 1:
            sil = d / f"assets-vs/gap{k}.wav"
            F.subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", str(GAP_S), str(sil)], check=True)
            seq.append(f"file '{sil.resolve()}'")
    (d / "assets-vs/list.txt").write_text("\n".join(seq) + "\n")
    (d / "assets").mkdir(exist_ok=True)
    F.subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(d / "assets-vs/list.txt"),
                      "-ar", "24000", "-ac", "1", str(d / "assets/narration.wav")], check=True)
    (d / "timings.json").write_text(json.dumps(full, indent=2))
    (d / "chapters.json").write_text(json.dumps(info, indent=2))


def build(slug: str, kw: dict) -> None:
    d = F.VIDEOS / slug
    (d / "compositions").mkdir(exist_ok=True)
    shutil.copy(F.HERE / "prompts/long/style.md", d / "style.md")
    todo = [c for c in chapters(d) if not F.fresh(d / f"compositions/{c['id']}.html", d / "assets/narration.wav")]

    def one(c: dict) -> None:
        F.ask(F.fill("long/build_chapter", chapter=c["id"], chapter_title=c["title"], goal=c["goal"],
                     visual_idea=c["visual_idea"], **{k: kw[k] for k in ("slug",)}), BUDGET["chapter"], c["id"])
        if not (d / f"compositions/{c['id']}.html").exists():
            raise F.StageError(f"{c['id']}: no composition written")
    with ThreadPoolExecutor(max_workers=len(todo) or 1) as ex:
        for f in [ex.submit(one, c) for c in todo]:
            f.result()
    if not F.fresh(d / f"out/{slug}.mp4", d / "assets/narration.wav"):
        F.setst(slug, "build", "run", "stitching + rendering")
        F.ask(F.fill("long/stitch", slug=slug), BUDGET["stitch"], "stitch")
        if not (d / f"out/{slug}.mp4").exists():
            raise F.StageError("stitch finished without the mp4")


def pipeline(slug: str, minutes: int, nchap: int) -> None:
    d, topic = F.VIDEOS / slug, json.loads((F.VIDEOS / slug / "topic.json").read_text())
    words = minutes * WPM
    kw = dict(slug=slug, working_title=topic["working_title"], angle=topic["angle"], minutes=minutes, words=words, chapters=nchap)
    try:
        if not done(slug, "outline"):
            F.setst(slug, "outline", "run", "research + chapter plan")
            F.ask(F.fill("long/outline", **kw), BUDGET["outline"], "outline")
            if not (d / "outline.json").exists():
                raise F.StageError("outline: no outline.json")
        F.setst(slug, "outline", "done")
        revision = ""
        for attempt in range(3):   # script -> independent fact check, up to 2 rewrites
            if not (done(slug, "script") and attempt == 0):
                F.setst(slug, "script", "run", "writing chapters" if attempt == 0 else f"rewriting after fact-check ({attempt})")
                F.ask(F.fill("long/script", revision=revision, **kw), BUDGET["script"], "script")
                write_script(d, words)
            F.setst(slug, "script", "done")
            if done(slug, "facts"):
                F.setst(slug, "facts", "done")
                break
            F.setst(slug, "facts", "run", "independent agent checking claims")
            F.ask(F.fill("long/facts", **kw), BUDGET["facts"], "facts")
            facts = json.loads((d / "facts.json").read_text())
            if facts.get("ok"):
                F.setst(slug, "facts", "done", "all claims verified")
                break
            revision = ("A fact-checker found these issues. Fix the chapter files in script/ and SOURCES.md accordingly "
                        "(keep each chapter's length):\n" + json.dumps(facts.get("issues", [])))
            if attempt == 2:
                raise F.StageError("facts: blocking issues after 2 rewrites")
        if not done(slug, "voice"):
            F.setst(slug, "voice", "run", "narrating chapters")
            try:
                F.urllib.request.urlopen("http://localhost:3900/.well-known/voicestudio-speech", timeout=3)
            except OSError:
                raise F.StageError("VoiceStudio app is not running")
            narrate_chapters(slug)
        F.setst(slug, "voice", "done")
        if not done(slug, "build"):
            F.setst(slug, "build", "run", "chapter agents in parallel")
            build(slug, kw)
        F.setst(slug, "build", "done")
        if not done(slug, "verify"):
            F.setst(slug, "verify", "run", "transcribing the render vs the script")
            r = F.tool("tools/shorts.py", "verify", f"videos/{slug}/out/{slug}.mp4", f"videos/{slug}/script.txt")
            if r.returncode:
                raise F.StageError("verify FAILED: " + r.stdout[-200:])
            (d / ".verified").write_text(datetime.now().isoformat())
        F.setst(slug, "verify", "done")
        if not done(slug, "meta"):
            F.setst(slug, "meta", "run", "title, description, chapters, thumbnail")
            F.ask(F.fill("long/meta", **kw), BUDGET["meta"], "meta")
            if not done(slug, "meta"):
                raise F.StageError("meta: missing metadata.json or thumbnail.png")
        F.setst(slug, "meta", "done")
        F.setst(slug, "review", "wait", "ready: waiting for your approval")
    except F.StageError as e:
        with F.lock:
            cur = next((s for s in STAGES if F.state[slug]["stages"][s] == "run"), "outline")
            F.state[slug]["stages"][cur] = "fail"
            F.state[slug]["err"] = str(e)
        F.beacon(slug, "blocked", str(e))
        F.log(f"✖ {slug}: {e}")
    except Exception as e:   # unexpected: show it, do not swallow
        with F.lock:
            cur = next((s for s in STAGES if F.state[slug]["stages"][s] == "run"), "outline")
            F.state[slug]["stages"][cur] = "fail"
            F.state[slug]["err"] = f"{type(e).__name__}: {e}"
        F.log(f"✖ {slug}: {type(e).__name__}: {e}")


def run(a: argparse.Namespace) -> None:
    slug, _, angle = a.topic.partition(":")
    slug = slug.strip()
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,29}", slug):
        sys.exit(f"bad slug {slug!r}: lowercase letters, digits, dashes")
    d = F.VIDEOS / slug
    d.mkdir(exist_ok=True)
    (d / "topic.json").write_text(json.dumps({"slug": slug, "working_title": slug.replace("-", " ").title(),
                                              "angle": angle.strip() or "explain it clearly with a point of view", "format": "long"}, indent=2))
    F.state[slug] = {"stages": {s: "todo" for s in STAGES}, "msg": "queued"}
    t0 = time.time()
    ex = ThreadPoolExecutor(max_workers=1)
    fut = ex.submit(pipeline, slug, a.minutes, a.chapters)
    try:
        with Live(F.view(1, t0), console=F.console, refresh_per_second=8) as live:
            while not fut.done():
                live.update(F.view(1, t0))
                time.sleep(0.12)
            live.update(F.view(1, t0))
    except KeyboardInterrupt:
        for p in list(F.procs):
            p.kill()
        ex.shutdown(wait=False, cancel_futures=True)
        F.console.print("[red]stopped. Run again to resume: finished stages are skipped.[/red]")
        return
    st = F.state[slug]
    F.console.print(f"\n{'[bold green]ready for review[/bold green]' if st['stages']['review'] == 'wait' else '[red]blocked: ' + st.get('err', '') + '[/red]'}"
                    f", ${F.total['cost']:.2f} spent. Next: factory/run.sh review")


def watch(_: argparse.Namespace) -> None:
    F.WATCH_FORMAT, F.done_check = "long", done   # read-only live view of long-form runs
    F.watch(_)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--topic", required=True, help='"slug:angle"')
    r.add_argument("--minutes", type=int, default=5)
    r.add_argument("--chapters", type=int, default=5)
    sub.add_parser("watch")
    a = ap.parse_args()
    {"run": run, "watch": watch}[a.cmd](a)

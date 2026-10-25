#!/usr/bin/env python3
"""Built by Agents video factory: auto-picks topics, runs the whole pipeline with live terminal view.

  factory.py run --count 3          pick 3 topics, show them, then run script > facts > voice > build > verify > meta
  factory.py run --count 3 --yes    skip the topic confirmation
  factory.py run --topics "slug:angle;slug2:angle2"   your own topics instead of auto-picked ones
  factory.py review                 watch each finished video, approve -> uploads private + scheduled
  factory.py status                 one-shot table
Uses `claude -p` (headless Claude Code) for the creative stages, so it uses your Claude plan/credit; every
call has a spending cap and the run prints the cost. Nothing is uploaded until you approve in `review`.
Run with clipper's venv (has rich + the Google libs):  factory/run.sh run --count 3
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import threading
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from pathlib import Path

from rich.console import Console, Group
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

ROOT = Path(__file__).resolve().parent.parent
HERE = Path(__file__).resolve().parent
VIDEOS = ROOT / "videos"
STAGES = ["script", "facts", "voice", "build", "verify", "meta", "review"]
BUDGET = {"plan": 1.5, "script": 2.5, "facts": 2.5, "build": 8.0, "meta": 1.0}   # USD cap per claude call
SPIN = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
MANILA = timezone(timedelta(hours=8))
SLOT_HOURS = (9, 21)
console = Console()
lock = threading.Lock()
state: dict[str, dict] = {}
log_lines: list[str] = []
total = {"cost": 0.0, "tokens": 0, "calls": 0}
procs: set = set()


class StageError(Exception):
    pass


def log(msg: str) -> None:
    with lock:
        log_lines.append(f"{datetime.now().strftime('%H:%M:%S')}  {msg}")
        del log_lines[:-60]


def beacon(slug: str, stage: str, msg: str = "") -> None:   # the web dashboard reads these too
    (VIDEOS / slug / "status.json").write_text(json.dumps({"stage": stage, "message": msg, "at": time.time()}))


def setst(slug: str, stage: str, status: str, msg: str = "") -> None:
    with lock:
        state[slug]["stages"][stage] = status
        t0, dur = state[slug].setdefault("t0", {}), state[slug].setdefault("dur", {})
        if status == "run":
            t0[stage] = time.time()
        elif stage in t0 and stage not in dur:
            dur[stage] = time.time() - t0[stage]
        took = dur.get(stage)
        if msg:
            state[slug]["msg"] = msg
    if status == "run":
        log(f"▶ {slug}: {stage} started" + (f" · {msg}" if msg else ""))
    elif status == "done" and took:
        log(f"✔ {slug}: {stage} done in {took:.0f}s")
    beacon(slug, stage, msg)


def ask(prompt: str, budget: float, tag: str) -> str:
    cmd = ["claude", "-p", prompt, "--output-format", "json", "--allowedTools", "Bash,Read,Write,Edit,WebFetch,WebSearch",
           "--permission-mode", "acceptEdits", "--max-budget-usd", str(budget)]
    p = subprocess.Popen(cmd, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    procs.add(p)
    try:
        out, err = p.communicate(timeout=2700)
    except subprocess.TimeoutExpired:
        p.kill()
        raise StageError(f"{tag}: claude timed out")
    finally:
        procs.discard(p)
    try:
        d = json.loads(out)
    except ValueError:
        raise StageError(f"{tag}: claude gave no JSON: {(err or out)[-160:]}")
    u = d.get("usage", {})
    with lock:
        total["cost"] += d.get("total_cost_usd") or 0
        total["tokens"] += u.get("input_tokens", 0) + u.get("output_tokens", 0) + u.get("cache_creation_input_tokens", 0)
        total["calls"] += 1
    if d.get("is_error"):
        raise StageError(f"{tag}: {str(d.get('result'))[:160]}")
    return str(d.get("result", "")).strip()


def tool(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, *args], cwd=ROOT, capture_output=True, text=True)


def fresh(a: Path, b: Path) -> bool:
    return a.exists() and b.exists() and a.stat().st_mtime >= b.stat().st_mtime


def done_check(slug: str, stage: str) -> bool:
    d = VIDEOS / slug
    sc, nar, mp4 = d / "script.txt", d / "assets/narration.wav", d / f"out/{slug}.mp4"
    facts = json.loads((d / "facts.json").read_text()) if (d / "facts.json").exists() else {}
    return {"script": sc.exists() and (d / "SOURCES.md").exists(),
            "facts": bool(facts.get("ok")) and fresh(d / "facts.json", sc),
            "voice": fresh(nar, sc) and (d / "timings.json").exists(),
            "build": fresh(mp4, nar),
            "verify": fresh(d / ".verified", mp4),
            "meta": (d / "metadata.json").exists()}.get(stage, False)


def fill(name: str, **kw) -> str:
    return (HERE / "prompts" / f"{name}.md").read_text().format(**kw)


def pipeline(slug: str) -> None:
    d, topic = VIDEOS / slug, json.loads((VIDEOS / slug / "topic.json").read_text())
    kw = dict(slug=slug, working_title=topic["working_title"], angle=topic["angle"], style=topic.get("style", "diagram"),
              remix=f"Credit/technique inspiration: {topic['repo_remix']} (awesome-opus5-5-videos)." if topic.get("repo_remix") else "")
    try:
        revision = ""
        for attempt in range(3):   # script -> independent fact check, up to 2 rewrites
            if not (done_check(slug, "script") and attempt == 0):
                setst(slug, "script", "run", "writing + sourcing script" if attempt == 0 else f"rewriting after fact-check ({attempt})")
                ask(fill("script", revision=revision, **kw), BUDGET["script"], "script")
                words = len((d / "script.txt").read_text().split())
                if not 35 <= words <= 85:
                    raise StageError(f"script has {words} words")
            setst(slug, "script", "done")
            if done_check(slug, "facts"):
                setst(slug, "facts", "done")
                break
            setst(slug, "facts", "run", "independent agent checking claims")
            ask(fill("facts", **kw), BUDGET["facts"], "facts")
            facts = json.loads((d / "facts.json").read_text())
            if facts.get("ok"):
                setst(slug, "facts", "done", "all claims verified")
                break
            revision = "A fact-checker found these issues. Fix script.txt and SOURCES.md accordingly (keep it 45-70 words):\n" + json.dumps(facts.get("issues", []))
            blocking = [i for i in facts.get("issues", []) if i.get("severity") == "blocking"]
            if attempt == 2:
                raise StageError(f"facts: {len(blocking)} blocking issue(s) after 2 rewrites")
        if not done_check(slug, "voice"):
            setst(slug, "voice", "run", "narrating in BuiltByAgentsExplainer voice")
            try:
                urllib.request.urlopen("http://localhost:3900/.well-known/voicestudio-speech", timeout=3)
            except OSError:
                raise StageError("VoiceStudio app is not running")
            r = tool("tools/shorts.py", "narrate", f"videos/{slug}/script.txt", f"videos/{slug}/assets-vs",
                     "--engine", "voicestudio", "--voice", "BuiltByAgentsExplainer")
            if r.returncode:
                raise StageError("voice: " + (r.stdout + r.stderr)[-200:])
            (d / "assets").mkdir(exist_ok=True)
            shutil.copy(d / "assets-vs/narration.wav", d / "assets/narration.wav")
            shutil.copy(d / "assets-vs/timings.json", d / "timings.json")
        setst(slug, "voice", "done")
        if not done_check(slug, "build"):
            setst(slug, "build", "run", "agent building the animation")
            ask(fill("build", **kw), BUDGET["build"], "build")
            if not (d / f"out/{slug}.mp4").exists():
                raise StageError("build finished without out/%s.mp4" % slug)
        setst(slug, "build", "done")
        if not done_check(slug, "verify"):
            setst(slug, "verify", "run", "transcribing the render vs the script")
            r = tool("tools/shorts.py", "verify", f"videos/{slug}/out/{slug}.mp4", f"videos/{slug}/script.txt")
            if r.returncode:
                raise StageError("verify FAILED: " + r.stdout[-200:])
            (d / ".verified").write_text(datetime.now().isoformat())
        setst(slug, "verify", "done", (r.stdout.splitlines() or [""])[0] if not done_check(slug, "verify") else "")
        if not done_check(slug, "meta"):
            setst(slug, "meta", "run", "title, description, tags")
            ask(fill("meta", **kw), BUDGET["meta"], "meta")
            if not (d / "metadata.json").exists():
                raise StageError("meta: no metadata.json")
        setst(slug, "meta", "done")
        setst(slug, "review", "wait", "ready: waiting for your approval")
    except StageError as e:
        with lock:
            cur = next((s for s in STAGES if state[slug]["stages"][s] == "run"), "script")
            state[slug]["stages"][cur] = "fail"
            state[slug]["err"] = str(e)
        beacon(slug, "blocked", str(e))
        log(f"✖ {slug}: {e}")
    except Exception as e:   # unexpected: show it, do not swallow
        with lock:
            cur = next((s for s in STAGES if state[slug]["stages"][s] == "run"), "script")
            state[slug]["stages"][cur] = "fail"
            state[slug]["err"] = f"{type(e).__name__}: {e}"
        log(f"✖ {slug}: {type(e).__name__}: {e}")


AGENT = {"script": "script-writer", "facts": "fact-checker", "voice": "voice · VoiceStudio", "build": "animation-builder",
         "verify": "audio-verifier", "meta": "metadata-writer", "review": "you"}
WORK = STAGES[:-1]   # stages that count as work; review is the human gate


def mmss(sec: float) -> str:
    return f"{int(sec) // 60}:{int(sec) % 60:02d}"


def flow(rows: list, now: float) -> Text:
    """The pipeline as boxes joined by connectors; a bright pulse runs along every active connector."""
    n = len(rows)
    cnt = {s: {"done": 0, "run": 0, "fail": 0, "wait": 0} for s in STAGES}
    for _, st, *_ in rows:
        for s in STAGES:
            if st[s] in cnt[s]:
                cnt[s][st[s]] += 1
    lines = [Text(), Text(), Text(), Text()]
    pos = int(now * 7) % 4
    for i, s in enumerate(STAGES):
        c = cnt[s]
        active = c["run"] > 0
        col = "yellow" if active else "red" if c["fail"] else "cyan" if c["wait"] else "green" if c["done"] else "grey50"
        spin = SPIN[int(now * 10) % len(SPIN)]
        status = (f"{spin} {c['run']}" if active else f"✖ {c['fail']}" if c["fail"] else f"● {c['wait']}" if c["wait"]
                  else f"✔ {c['done']}" if c["done"] else "○")
        name = "YOU" if s == "review" else s.upper()
        lines[0].append("╭" + "─" * 9 + "╮", col)
        lines[1].append("│" + name.center(9) + "│", f"bold {col}")
        lines[2].append("│" + status.center(9) + "│", col)
        lines[3].append("╰" + "─" * 9 + "╯", col)
        if i < len(STAGES) - 1:
            nxt = cnt[STAGES[i + 1]]
            flowing = active or (c["done"] > 0 and (nxt["run"] > 0 or nxt["done"] < c["done"]))
            for k, ln in enumerate(lines):
                if k == 1:
                    cells = ["━", "━", "━", "▶"]
                    if flowing:
                        cells = ["●" if j == pos and j < 3 else "━" for j in range(3)] + ["▶"]
                    ln.append("".join(cells), "bold yellow" if flowing else "green" if c["done"] else "grey37")
                else:
                    ln.append("    ")
    return Text("\n").join(lines)


def view(count: int, t0: float, watching: bool = False) -> Group:
    now = time.time()
    with lock:
        rows = [(k, dict(v["stages"]), v["msg"], v.get("err", ""), dict(v.get("t0", {})), dict(v.get("dur", {})))
                for k, v in state.items()]
        lines, cost, tok, calls = log_lines[-9:], total["cost"], total["tokens"], total["calls"]
    done_n = sum(1 for r in rows for s in WORK if r[1][s] == "done")
    pct = done_n / max(len(rows) * len(WORK), 1)
    working = sum(1 for r in rows if "run" in r[1].values())
    el = mmss(now - t0)
    stats = (f"{len(rows)} videos · {working} working now · {'watching' if watching else 'elapsed'} {el}" if watching else
             f"{len(rows)} videos · {working} agents working · elapsed {el} · {calls} calls · {tok // 1000}k tokens · ${cost:.2f}")
    bar = Text("  ")
    full = int(pct * 36)
    bar.append("█" * full, "green").append("░" * (36 - full), "grey23").append(f"  {int(pct * 100)}%  ({done_n}/{len(rows) * len(WORK)} stages)", "bold")
    head = Panel(Group(Text(stats, "bold"), bar), title="[bold green]BUILT BY AGENTS · FACTORY[/]", border_style="green")

    lanes = Table(box=None, pad_edge=False, expand=True, show_header=True, header_style="dim")
    lanes.add_column("video", style="bold", no_wrap=True)
    lanes.add_column("pipeline", no_wrap=True)
    lanes.add_column("now", ratio=1, overflow="ellipsis", no_wrap=True)
    for slug, st, msg, err, st0, dur in rows:
        bar_t = Text()
        for s in STAGES:
            v = st[s]
            bar_t.append("▰▰ " if v in ("done", "run", "fail", "wait") else "▱▱ ",
                         "green" if v == "done" else "bold yellow" if v == "run" else "bold red" if v == "fail" else "cyan" if v == "wait" else "grey37")
        cur = next((s for s in STAGES if st[s] in ("run", "fail")), None)
        if err:
            what = Text(f"✖ {err}", "red")
        elif cur:
            what = Text(f"{SPIN[int(now * 10) % len(SPIN)]} {cur}  {mmss(now - st0[cur]) if cur in st0 else ''}  {msg}", "yellow")
        elif st["review"] == "wait":
            what = Text("● READY · waiting for your approval (factory/run.sh review)", "bold cyan")
        else:
            what = Text(msg or "queued", "grey50")
        lanes.add_row(slug, bar_t, what)

    ag = Table(box=None, pad_edge=False, expand=True, show_header=False)
    ag.add_column(width=2); ag.add_column(width=22); ag.add_column(width=22); ag.add_column(ratio=1)
    busy = [(r[0], s, r[4].get(s)) for r in rows for s in STAGES if r[1][s] == "run"]
    for slug, s, started in busy:
        ag.add_row(Text(SPIN[int(now * 10) % len(SPIN)], "yellow"), Text(AGENT[s], "bold"), slug, Text(mmss(now - started) if started else "", "dim"))
    if not busy:
        ag.add_row("", Text("no agents working", "grey50"), "", "")
    colored = Text()
    for ln in lines:
        stamp, _, rest = ln.partition("  ")
        colored.append(stamp + "  ", "grey50").append(rest + "\n", "red" if "✖" in rest else "green" if rest.startswith("✔") else "white")
    return Group(head, Panel(flow(rows, now), title="workflow", border_style="grey37"), Panel(lanes, title="videos", border_style="grey37"),
                 Panel(ag, title="agents", border_style="grey37"), Panel(colored if lines else Text("starting…", "grey50"), title="live log", border_style="grey37"))


def existing_context() -> tuple[str, str]:
    names = sorted(p.name for p in VIDEOS.iterdir() if p.is_dir())
    titles = []
    for n in names:
        m = VIDEOS / n / "metadata.json"
        titles.append(f"{n}: {json.loads(m.read_text())['title']}" if m.exists() else n)
    perf = ""
    try:
        from google.oauth2.credentials import Credentials
        from googleapiclient.discovery import build
        led = json.loads((ROOT / "publish/uploaded.json").read_text())
        yt = build("youtube", "v3", credentials=Credentials.from_authorized_user_file(
            str(ROOT / "tools/.yt/token.json"), ["https://www.googleapis.com/auth/youtube"]), cache_discovery=False)
        items = yt.videos().list(part="statistics", id=",".join(v["video_id"] for v in led.values())).execute()["items"]
        inv = {v["video_id"]: k for k, v in led.items()}
        perf = ", ".join(f"{inv[i['id']]}: {i['statistics'].get('viewCount', 0)} views" for i in items)
    except Exception:
        perf = ""
    return "; ".join(titles), perf or "no data yet (nothing public long enough)"


def plan_topics(count: int) -> list[dict]:
    existing, perf = existing_context()
    out = ask(fill("plan", count=count, existing=existing, performance=perf), BUDGET["plan"], "plan")
    topics = json.loads(out[out.index("["):out.rindex("]") + 1])
    for t in topics:
        t["slug"] = re.sub(r"[^a-z0-9-]", "", t["slug"].lower())[:30].strip("-")
    return [t for t in topics if t["slug"] and not (VIDEOS / t["slug"]).exists()][:count]


def run(a: argparse.Namespace) -> None:
    for cmd in ("claude", "npx", "ffmpeg"):
        if not shutil.which(cmd):
            sys.exit(f"missing: {cmd}")
    if a.topics:
        topics = []
        for part in a.topics.split(";"):
            slug, _, angle = part.partition(":")
            if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,29}", slug.strip()):
                sys.exit(f"bad topic slug {slug.strip()!r}: use lowercase letters, digits and dashes; separate topics with ';' and never use ';' inside the angle")
            topics.append({"slug": slug.strip(), "working_title": slug.strip().replace("-", " ").title(),
                           "angle": angle.strip() or "explain it clearly with a point of view", "style": "diagram"})
    else:
        with console.status("[bold green]picking topics (planner agent, checks what exists and what performed)…"):
            topics = plan_topics(a.count)
    if not topics:
        sys.exit("no topics to run")
    tbl = Table(title="Topics for this run", show_lines=False)
    for c in ("#", "slug", "style", "angle"):
        tbl.add_column(c)
    for i, t in enumerate(topics, 1):
        tbl.add_row(str(i), t["slug"], t.get("style", ""), t["angle"][:90])
    console.print(tbl)
    if not a.yes:
        ans = console.input("Start? [Enter = yes, 'drop 2 4' to remove, n = cancel] ").strip().lower()
        if ans == "n":
            return
        if ans.startswith("drop"):
            drop = {int(x) for x in ans.split()[1:] if x.isdigit()}
            topics = [t for i, t in enumerate(topics, 1) if i not in drop]
    for t in topics:
        (VIDEOS / t["slug"]).mkdir(exist_ok=True)
        (VIDEOS / t["slug"] / "topic.json").write_text(json.dumps(t, indent=2))
        state[t["slug"]] = {"stages": {s: "todo" for s in STAGES}, "msg": "queued"}
    t0 = time.time()
    ex = ThreadPoolExecutor(max_workers=a.concurrency)
    futs = [ex.submit(pipeline, t["slug"]) for t in topics]
    try:
        with Live(view(len(topics), t0), console=console, refresh_per_second=8, transient=False) as live:
            while not all(f.done() for f in futs):
                live.update(view(len(topics), t0))
                time.sleep(0.12)
            live.update(view(len(topics), t0))
    except KeyboardInterrupt:
        for p in list(procs):
            p.kill()
        ex.shutdown(wait=False, cancel_futures=True)
        console.print("[red]stopped. Run again to resume: finished stages are skipped.[/red]")
        return
    ready = [k for k, v in state.items() if v["stages"]["review"] == "wait"]
    bad = [k for k, v in state.items() if "fail" in v["stages"].values()]
    console.print(f"\n[bold green]{len(ready)} ready for review[/bold green], [red]{len(bad)} blocked[/red], ${total['cost']:.2f} spent. "
                  f"Next: [bold]factory/run.sh review[/bold]")


def next_slot(after: datetime) -> datetime:
    day = after.astimezone(MANILA).replace(minute=0, second=0, microsecond=0)
    for i in range(0, 60):
        for h in SLOT_HOURS:
            c = (day + timedelta(days=i)).replace(hour=h)
            if c > after:
                return c
    raise RuntimeError("no slot")


def review(_: argparse.Namespace) -> None:
    led = json.loads((ROOT / "publish/uploaded.json").read_text()) if (ROOT / "publish/uploaded.json").exists() else {}
    ready = [p.name for p in sorted(VIDEOS.iterdir()) if (p / ".verified").exists() and (p / "metadata.json").exists() and p.name not in led]
    if not ready:
        return console.print("nothing waiting for review")
    last = max([datetime.fromisoformat(v["publish_at"]) for v in led.values()] + [datetime.now(timezone.utc)])
    for slug in ready:
        m = json.loads((VIDEOS / slug / "metadata.json").read_text())
        slot = next_slot(last + timedelta(minutes=30))
        console.print(Panel(f"[bold]{m['title']}[/bold]\n\n{m['description']}\n\n[dim]tags: {', '.join(m['tags'])}\nschedule: {slot:%a %d %b %H:%M} Manila[/dim]", title=slug))
        subprocess.run(["open", str(VIDEOS / slug / f"out/{slug}.mp4")])
        ans = console.input("[bold]approve and upload (private + scheduled)? [y/N/q][/bold] ").strip().lower()
        if ans == "q":
            break
        if ans != "y":
            continue
        m["publish_at"] = slot.isoformat()
        (VIDEOS / slug / "metadata.json").write_text(json.dumps(m, indent=2, ensure_ascii=False))
        r = tool("tools/upload.py", slug, "--go")
        console.print(r.stdout[-400:] or r.stderr[-400:])
        if r.returncode == 0:
            last = slot


WATCH_FORMAT = "short"   # long.py sets "long" so its watch shows only long-form runs
BEACON_STAGE = {"scripting": "script", "building": "build", "checking": "build", "rendering": "build", "verifying": "verify"}


def watch(_: argparse.Namespace) -> None:
    """Read-only live view of any factory run (reads files + beacons, spends nothing). Ctrl+C to leave."""
    t0 = time.time()
    with Live(console=console, refresh_per_second=4) as live:
        while True:
            led = json.loads((ROOT / "publish/uploaded.json").read_text()) if (ROOT / "publish/uploaded.json").exists() else {}
            new = {}
            for p in sorted(VIDEOS.iterdir()):
                if not (p / "topic.json").exists() or p.name in led:
                    continue
                if json.loads((p / "topic.json").read_text()).get("format", "short") != WATCH_FORMAT:
                    continue
                b = json.loads((p / "status.json").read_text()) if (p / "status.json").exists() else {}
                live_b = time.time() - b.get("at", 0) < 600
                cur = BEACON_STAGE.get(b.get("stage"), b.get("stage")) if live_b else None
                st = {s: ("done" if done_check(p.name, s) else "todo") for s in STAGES[:-1]}
                st["review"] = "wait" if all(v == "done" for v in st.values()) and (p / ".verified").exists() else "todo"
                if cur in st and cur != "review" and st[cur] != "done":
                    st[cur] = "run"
                if b.get("stage") == "blocked" and live_b:
                    st[next((s for s in STAGES if st[s] != "done"), "script")] = "fail"
                new[p.name] = {"stages": st, "msg": b.get("message", "") if live_b else "", "err": b.get("message", "") if b.get("stage") == "blocked" and live_b else ""}
            with lock:
                state.clear()
                state.update(new)
            live.update(view(len(new), t0, watching=True))
            time.sleep(0.5)


def status(_: argparse.Namespace) -> None:
    t = Table("video", "script", "facts", "voice", "build", "verify", "meta", "uploaded")
    led = json.loads((ROOT / "publish/uploaded.json").read_text()) if (ROOT / "publish/uploaded.json").exists() else {}
    for p in sorted(VIDEOS.iterdir()):
        if (p / "script.txt").exists():
            t.add_row(p.name, *["✔" if done_check(p.name, s) else "·" for s in STAGES[:-1]], "✔" if p.name in led else "·")
    console.print(t)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--count", type=int, default=3)
    r.add_argument("--concurrency", type=int, default=3)
    r.add_argument("--topics")
    r.add_argument("--yes", action="store_true")
    sub.add_parser("review")
    sub.add_parser("status")
    sub.add_parser("watch")
    a = ap.parse_args()
    try:
        {"run": run, "review": review, "status": status, "watch": watch}[a.cmd](a)
    except KeyboardInterrupt:
        pass

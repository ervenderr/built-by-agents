#!/usr/bin/env python3
"""Upload finished videos to the channel as PRIVATE + scheduled (publishAt), from videos/<name>/metadata.json.

  upload.py NAME [NAME ...]          dry run (default): checks everything, uploads nothing
  upload.py NAME [NAME ...] --go     really upload (needs the new channel's token; see TOKEN)
Run it with clipper's venv, which has google-api-python-client:
  ~/Projects/clipper/.venv/bin/python tools/upload.py agent-loop

Safety: refuses unless metadata is valid and `shorts.py verify` passes on the video's own script.
Already-uploaded names (publish/uploaded.json) are skipped. Never makes a video public by itself.
"""
import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKEN = ROOT / "tools/.yt/token.json"   # from tools/yt_auth.py (scope: youtube); confirmed: Built by Agents @builtbyagents12
LEDGER = ROOT / "publish/uploaded.json"
SCOPE = ["https://www.googleapis.com/auth/youtube"]
MAX_TITLE, MAX_DESC, MAX_TAGS = 100, 5000, 500


def load_meta(name: str) -> dict:
    m = json.loads((ROOT / f"videos/{name}/metadata.json").read_text())
    errs = []
    if not 0 < len(m["title"]) <= MAX_TITLE:
        errs.append("title length")
    if not 0 < len(m["description"]) <= MAX_DESC:
        errs.append("description length")
    if len(",".join(m["tags"])) > MAX_TAGS:
        errs.append("tags over 500 chars")
    if "<" in m["title"] + m["description"] or ">" in m["title"] + m["description"]:
        errs.append("< or > not allowed by YouTube")
    when = datetime.fromisoformat(m["publish_at"])
    if when <= datetime.now(timezone.utc):
        errs.append("publish_at is in the past")
    if errs:
        sys.exit(f"{name}: invalid metadata: {', '.join(errs)}")
    return m


def verified(name: str) -> bool:
    d = ROOT / f"videos/{name}"
    r = subprocess.run([sys.executable, str(ROOT / "tools/shorts.py"), "verify", str(d / f"out/{name}.mp4"),
                        str(d / "script.txt")], capture_output=True, text=True)
    print(f"  verify: {r.stdout.splitlines()[0] if r.stdout else r.stderr[-200:]}")
    return r.returncode == 0


def upload(name: str, m: dict) -> str:
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
    creds = Credentials.from_authorized_user_file(str(TOKEN), SCOPE)
    yt = build("youtube", "v3", credentials=creds)
    body = {"snippet": {"title": m["title"], "description": m["description"], "tags": m["tags"],
                        "categoryId": m["category_id"]},
            "status": {"privacyStatus": "private",
                       "publishAt": datetime.fromisoformat(m["publish_at"]).astimezone(timezone.utc)
                       .strftime("%Y-%m-%dT%H:%M:%S.000Z"),
                       "selfDeclaredMadeForKids": m["made_for_kids"],
                       "containsSyntheticMedia": m["synthetic_media"]}}
    media = MediaFileUpload(str(ROOT / f"videos/{name}/out/{name}.mp4"), mimetype="video/mp4", resumable=True)
    req = yt.videos().insert(part="snippet,status", body=body, media_body=media)
    resp = None
    while resp is None:
        _, resp = req.next_chunk()
    thumb = ROOT / f"videos/{name}/{m['thumbnail']}" if m.get("thumbnail") else None
    if thumb:   # long-form only; needs a verified channel
        yt.thumbnails().set(videoId=resp["id"], media_body=MediaFileUpload(str(thumb))).execute()
    return resp["id"]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("names", nargs="+")
    ap.add_argument("--go", action="store_true")
    a = ap.parse_args()
    ledger = json.loads(LEDGER.read_text()) if LEDGER.exists() else {}
    for name in a.names:
        print(name)
        if name in ledger:
            print(f"  skip: already uploaded as {ledger[name]['video_id']}")
            continue
        m = load_meta(name)
        if not verified(name):
            sys.exit(f"{name}: audio does not match script; not uploading")
        print(f"  title: {m['title']}\n  publish_at: {m['publish_at']}  tags: {len(m['tags'])}")
        if not a.go:
            print("  dry run: nothing uploaded")
            continue
        vid = upload(name, m)
        ledger[name] = {"video_id": vid, "publish_at": m["publish_at"],
                        "uploaded_at": datetime.now(timezone.utc).isoformat()}
        LEDGER.write_text(json.dumps(ledger, indent=2))
        print(f"  uploaded private + scheduled: https://studio.youtube.com/video/{vid}/edit")


if __name__ == "__main__":
    main()

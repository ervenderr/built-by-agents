#!/usr/bin/env python3
"""One-time login for the channel: saves tools/.yt/token.json with the `youtube` scope
(upload + edit/delete own videos + read status). Run with clipper's venv, then sign in as the
channel's Google account and pick the Built by Agents channel:
  ~/Projects/clipper/.venv/bin/python tools/yt_auth.py
"""
import os
from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow

HERE = Path(__file__).resolve().parent
CLIENT = Path.home() / "Projects/clipper/client_secret.json"   # Desktop OAuth client of project built-by-agents
OUT = HERE / ".yt/token.json"
SCOPES = ["https://www.googleapis.com/auth/youtube"]

if __name__ == "__main__":
    creds = InstalledAppFlow.from_client_secrets_file(str(CLIENT), SCOPES).run_local_server(port=0)
    OUT.parent.mkdir(exist_ok=True)
    fd = os.open(OUT, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as f:
        f.write(creds.to_json())
    print(f"saved {OUT}")

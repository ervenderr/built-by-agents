#!/usr/bin/env python3
"""Progress beacon for the dashboard: status.py NAME STAGE ["message"]  -> videos/NAME/status.json"""
import json
import sys
import time
from pathlib import Path

if len(sys.argv) < 3:
    sys.exit(__doc__)
name, stage, msg = sys.argv[1], sys.argv[2], " ".join(sys.argv[3:])
(Path(__file__).resolve().parent.parent / f"videos/{name}/status.json").write_text(
    json.dumps({"stage": stage, "message": msg, "at": time.time()}))

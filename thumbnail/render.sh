#!/usr/bin/env bash
# usage: ./render.sh out.png "AI TRIAGE *AGENT*" "NEVER LOSES A MESSAGE" /abs/path/screenshot.png
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
q() { python3 -c 'import sys,urllib.parse as u;print(u.quote(sys.argv[1]))' "$1"; }
url="file://$here/thumb.html?t=$(q "$2")&tag=$(q "${3:-}")&img=$(q "${4:+file://$4}")"
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu \
  --hide-scrollbars --window-size=1280,720 --virtual-time-budget=3000 --screenshot="$1" "$url" >/dev/null 2>&1
echo "wrote $1"

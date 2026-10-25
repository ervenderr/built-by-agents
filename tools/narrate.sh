#!/usr/bin/env bash
# usage: tools/narrate.sh "sentence or file.txt" out.wav [voice] [speed]
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
HYPERFRAMES_PYTHON="$here/tts-venv/bin/python" npx hyperframes tts "$1" -o "$2" --voice "${3:-af_heart}" --speed "${4:-1.0}"

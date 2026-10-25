#!/usr/bin/env bash
# usage: factory/run.sh run --count 3 | review | status | watch      (Shorts)
#        factory/run.sh long run --topic "slug:angle" [--minutes 5 --chapters 5]   (long-form)
#        factory/run.sh long watch   (live view of long-form runs, read-only)
here="$(cd "$(dirname "$0")" && pwd)"
py=~/Projects/clipper/.venv/bin/python
if [ "$1" = "long" ]; then shift; exec "$py" "$here/long.py" "$@"; fi
exec "$py" "$here/factory.py" "$@"

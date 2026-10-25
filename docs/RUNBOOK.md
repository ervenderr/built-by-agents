# Runbook: daily operations and fixes

## Every day
1. Make sure the **VoiceStudio** app is open (voice server `http://localhost:3900`).
2. `factory/run.sh review` for anything finished; approve with `y` (uploads private + scheduled).
3. When fewer than ~4 videos remain scheduled: `factory/run.sh run --count 7` (confirm or `drop 2 4` topics, then watch).
4. In YouTube Studio > Analytics, look at the first 48 h of each video; tell Claude what to make more of.

## Commands
| Command | What it does |
|---|---|
| `factory/run.sh run --count N [--concurrency 3] [--yes]` | Auto-pick N topics and run the whole pipeline with the live view. Ctrl+C is safe: finished stages are skipped next time |
| `factory/run.sh run --topics "slug-one:angle one;slug-two:angle two"` | Your own topics. Slugs are lowercase letters/digits/dashes; separate topics with `;` and never use `;` inside an angle |
| `factory/run.sh review` | Play each ready video, approve to upload |
| `factory/run.sh watch` | Read-only live view of any run (also works for runs started elsewhere) |
| `factory/run.sh status` | One-shot table of stages per video |
| `python3 tools/shorts.py narrate script.txt OUT --engine voicestudio --voice BuiltByAgentsExplainer [--fit old/timings.json]` | Narrate; `--fit` squeezes each sentence into an old slot (+/-25% tempo) so animations need no retiming |
| `python3 tools/shorts.py verify out/<slug>.mp4 script.txt` | PASS/FAIL: does the audio match the script |
| `~/Projects/clipper/.venv/bin/python tools/upload.py <slug> [--go]` | Dry run by default; `--go` uploads private + scheduled |
| `~/Projects/clipper/.venv/bin/python tools/yt_auth.py` | Re-login to YouTube (scope `youtube`); sign in as the channel account, pick Built by Agents |

The factory and upload tool run with clipper's Python (`~/Projects/clipper/.venv`), which has `rich` and the Google libraries. Clipper itself is not used for this channel; only its venv and `client_secret.json` (Desktop OAuth client of Google Cloud project `built-by-agents`) are referenced.

## Changing the schedule or deleting a video
Token scope `youtube` allows update/delete. Update `status.publishAt` with `videos.update(part="status")` (must also send `privacyStatus: "private"`). Studio shows the video as "Scheduled" when this works (confirmed).

## Troubleshooting
| Symptom | Cause / fix |
|---|---|
| "VoiceStudio app is not running" | Open the VoiceStudio app; check `curl localhost:3900/.well-known/voicestudio-speech` |
| HTTP 429 from the voice server | Parallel callers. `shorts.py` already serializes with a lock and retries; don't add parallel narrators |
| Voice changes between sentences/videos | Must use `--engine voicestudio --voice BuiltByAgentsExplainer` (seeded route). An unknown profile name silently falls back to a random voice; the transcription check catches garbage but not a wrong voice |
| `narrate` fails "sentence N mismatch" | Whisper misheard (e.g. a brand name). Hyphens and "chat gpt" are normalized; for new brand words add normalization in `tools/shorts.py` `words()` |
| Facts stage blocked | Open `videos/<slug>/facts.json`; fix the blocking issue by editing `script.txt` and `SOURCES.md`, delete `facts.json`, re-run the same topic (finished stages skip) |
| Build stage blocked | Read the agent message in the live log; `cd videos/<slug>` and run `npx hyperframes check --json` and `snapshot` to see |
| GSAP CDN timeout in `hyperframes check` | Transient network; retry |
| Upload "403 insufficient scopes" | Re-run `tools/yt_auth.py` (needs scope `youtube`) |
| Videos stay private after publish time | Check Studio > Content; API scheduling works without the API audit (confirmed). If it ever stops, apply for the YouTube API Services audit form (needs an https site with privacy policy and ToS) |
| Upload says `uploadLimitExceeded` | Channel-level upload cap (new/unverified channel). Check Studio > Upload for a reset time and verify the channel at youtube.com/verify; retry later. Not the API quota |
| `rich` import error | Run through `factory/run.sh` (uses clipper's venv) |

## Long-form commands
| Command | What it does |
|---|---|
| `factory/run.sh long run --topic "slug:angle" --minutes 5 --chapters 5` | Run the long-form pipeline for one topic (never use `;` in the angle) |
| `factory/run.sh long watch` | Read-only live view of long-form runs (the plain `watch` shows Shorts only) |
| `factory/run.sh review` | Approve and upload finished videos (long-form needs its own slot: set `publish_at` in `metadata.json` to 18:00 Manila first) |
| `caffeinate -dims -w <pid>` | Keep the Mac awake while a run is going (a closed lid still sleeps it) |

## Backups and cleanup
Intermediate narration (`assets-vs/`) and old renders can be deleted once a video is verified. `tools/.yt/` holds the OAuth token: never commit or share it.

## Replacing an uploaded video
1. Upload the new one first (`tools/upload.py NAME --go` after removing NAME from `publish/uploaded.json`; keep a backup of the ledger).
2. Only then delete the old id (YouTube API `videos().delete` with the token in `tools/.yt/`), after the owner approves.
3. If `uploadLimitExceeded`: wait and retry; old copies stay scheduled meanwhile (watch for ones about to go public).

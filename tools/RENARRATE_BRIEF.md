# Re-narrate an existing Short in the channel voice (BuiltByAgentsExplainer)

Work ONLY in `/Users/ervenderr/Projects/youtube-os/videos/<name>`. Do not touch other videos, ~/Projects/clipper, or the VoiceStudio profiles/settings. The VoiceStudio desktop app must stay running (local API on :3900); if the API call fails, say so and stop.

1. Back up the old render: copy `out/<name>.mp4` to `out/<name>.kokoro.mp4` (keep it, do not delete).
2. Write `script.txt` (one sentence per line) from the exact lines given in your task. This is the final narration.
3. Narrate: `python3 /Users/ervenderr/Projects/youtube-os/tools/shorts.py narrate script.txt assets-vs --engine voicestudio --voice BuiltByAgentsExplainer` (sequential; each sentence is verified by transcription; it fails loudly on a mismatch; never write your own loop). It writes `assets-vs/narration.wav` and `assets-vs/timings.json` (start and duration per sentence). Copy `assets-vs/narration.wav` to `assets/narration.wav`.
4. Retime the scenes and caption clips in `index.html` from `timings.json` (the new voice has different pacing than the old Kokoro one). Update every on-screen caption and label whose wording changed. Remove any 1.2x speed assumption. Set the root `data-duration` to the narration length plus about 2 s hold so the closing line stays on screen at least 2 s, and the audio element `data-duration` to the narration length.
5. `npx hyperframes check --json` must be ok:true with 0 errors. Snapshot 6+ moments and look at them (text hidden, overlaps, empty frames; frame 0 must show the hook). Fix problems.
6. `npx hyperframes render -o out/<name>.mp4`.
7. Verify: `python3 /Users/ervenderr/Projects/youtube-os/tools/shorts.py verify out/<name>.mp4 script.txt` must print PASS. If FAIL, fix and repeat.
8. Update the README.md narration line and voice line ("VoiceStudio profile BuiltByAgentsExplainer, The Explainer design voice, seed 42"). Do not change CREDITS.md or SOURCES.md except to add a line for any new wording that needs a source.
9. Final reply under 100 words: new duration, check counts, verify result (PASS/FAIL with ratio), anything unverified. Do not claim anything you did not run.

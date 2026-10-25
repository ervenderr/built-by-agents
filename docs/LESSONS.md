# Lessons: what broke, why, and what prevents it now

| What happened | Cause | Prevention now |
|---|---|---|
| Content built around the owner's own projects | Claude inferred the niche from the project folders and never asked | Direction is topic-driven animated explainers; ask before inferring content (memory note `youtube-builtbyagents`) |
| Narration repeated sentence 1 and dropped the last (2 videos) | A zsh loop used 0-based array indexing (zsh arrays are 1-based) | `tools/shorts.py narrate` is a Python loop; `verify` transcribes every render and compares it with the script |
| Voice differed between videos | The generic OpenAI-style speech route had no seed: pitch swung 96-212 Hz across sentences | Seeded `/generate` route (seed 42): spread 9 Hz inside a video, 5 Hz across 8 videos |
| HTTP 429 from the voice server | Four agents called it at once | Cross-process file lock + retry with backoff in `speak_voicestudio` |
| Unknown voice name produced garbage audio | The app falls back to a random voice | Transcription check on every sentence; always use the profile name `BuiltByAgents` |
| Fact checker blocked videos forever | Any wording nitpick set `ok:false` | Severity levels: only `blocking` (wrong/unverified/material overclaim) blocks |
| Voice check rejected "fixed-size" vs "fixed size" | Whisper drops hyphens | `ratio()` tries both readings; "chat gpt" normalized |
| A junk video "change one character and it scrambles" was created | `;` inside a `--topics` angle split it into a second topic | Slug validation (`[a-z0-9-]`) at the boundary |
| `review` cell spun forever in `watch` | The beacon stage "review" was treated as running | `watch` never marks review as running |
| Screenshot Shorts looked repetitive/cropped | Reused the same demo screenshots in a 9:16 crop | Superseded by original animated videos |
| 429/HTTP limits on first agent wave | Same as above | Run in waves; lock |
| Playing a video produced no sound for the owner | Playback surface, not the file (AAC 48 kHz stereo present, -17 dB mean) | Test with QuickTime / `afplay` |

## Facts that matter (verified during this project)
- YPP today: 1,000 subs + 4,000 public watch hours (12 months) or 10M Shorts views (90 days). From 2027-02-01 new applicants need 8,000 hours or 20M Shorts views. Shorts-feed watch time does not count toward the 4,000 hours (YouTube Help, support.google.com/youtube/answer/72851).
- API uploads from a new unaudited Google project can be restricted to private; scheduled publish still worked for this channel (confirmed in Studio).
- Shorts RPM is a small fraction of long-form RPM; ad revenue is a bonus, services/affiliates are the income (AIR data, `research/monetization.md`).
- Demand for the animation-as-format is unproven (competitor data showed code-rendered animated agent explainers at 18-79 views); Day 28 is the test.

## Open items
- Nobody has watched all videos end to end yet.
- Philippines eligibility for the partner program and fan funding is unverified: check YouTube Studio > Monetization. Tax (BIR, W-8BEN) needs an accountant.
- Long-form (16:9, 8-15 min) pipeline not built; Shorts do not count toward the 4,000 hours.

## 2026-10-25
| Problem | Cause | Fix |
|---|---|---|
| Upload fails `uploadLimitExceeded` ("exceeded the number of videos they may upload") | Daily/rolling upload cap on the channel after ~8 API uploads in a day; reset time not confirmed | Upload new videos before deleting old ones, retry after several hours; do not re-upload replacements in bulk on the same day as the first batch |
| Descriptions said "Kokoro" after switching voices | `meta.md` prompt hard-coded the old line | Change the voice line in `metadata.json` whenever the voice changes (all 7 fixed) |
| Narration check failed on digits ("13,002"), apostrophes ("weight\'s") and homophones ("wait" for "weight") | Whisper prints digits and guesses homophones where the narrator was right | `tools/shorts.py words()` spells numbers out and drops apostrophes; `HOMOPHONE` maps wait/weight on both sides |
| `--topics` run died: "bad topic slug" | A `;` inside an angle splits the topic list | Never put `;` in an angle; use commas |
| Clipped narration ("surely a bette") | VoiceStudio returned truncated audio for one sentence | Re-run: the sentence check fails loudly and finished stages are skipped |
| AI-only niche felt too narrow | Few viewers search for AI internals; competitors' code-rendered AI explainers got 18-79 views | Broad "how things work" topics (AI at most 1 in 5), engagement playbook in `research/` |

# Standing brief for a video-building agent (paste or reference this, plus topic and remix source)

Build ONE animated vertical Short (1080x1920, 18-28 s) with HyperFrames for the faceless channel Built by Agents. Work only in `/Users/ervenderr/Projects/youtube-os/videos/<name>`. Never touch ~/Projects/clipper or other projects.

1. Read `/Users/ervenderr/.claude/skills/hyperframes/SKILL.md` and its references (types/vertical.md, format.md, runtimes.md, captions.md, motion.md). Template that passes check: `videos/agent-loop/index.html`. Scaffold: `HYPERFRAMES_SKIP_SKILLS=1 npx hyperframes init <dir> --example blank --resolution portrait --non-interactive --skip-transcribe`.
2. Write `script.txt` in the video folder: one sentence per line, 45-70 words, a point of view, only facts you verified with a URL in `SOURCES.md`. Label any illustrative numbers "illustrative" on screen.
3. Narrate: `python3 /Users/ervenderr/Projects/youtube-os/tools/shorts.py narrate <dir>/script.txt <dir>/assets --engine voicestudio --voice BuiltByAgentsExplainer` (the channel voice; the VoiceStudio app must be running; seeded so it is identical every run; sequential, each sentence verified by transcription). It writes `assets/narration.wav` and `assets/timings.json` (start and duration per sentence); time scenes and captions from `timings.json`. Never write your own shell loop (zsh arrays are 1-based; this broke two videos).
4. Build index.html: text inside y 168-1330, captions near y 1190, frame 0 already shows the hook, dim colours contrast >= 3:1, moving objects never cover labels, last line on screen >= 2 s, `fromTo` not `from`, one paused root timeline.
5. `npx hyperframes check --json` must be ok:true with 0 errors; snapshot 6+ moments and look at them; fix; `npx hyperframes render -o out/<name>.mp4`.
6. Verify the render: `python3 tools/shorts.py verify <dir>/out/<name>.mp4 <dir>/script.txt` must print PASS.
7. Write `README.md` (topic, script, voice, what is unverified), `CREDITS.md` (repo author remixed + URL), `SOURCES.md`.
8. Final reply under 120 words: mp4 path, duration, script, check counts, verify result, anything unverified. Do not claim anything you did not run.

## Dashboard progress beacon (required)
At each stage run `python3 /Users/ervenderr/Projects/youtube-os/tools/status.py <name> <stage> "<short message>"` so the dashboard shows you working. Stages in order: `scripting`, `narrating`, `building`, `checking`, `rendering`, `verifying`, `done` (or `blocked` with the reason). Also write `videos/<name>/metadata.json` (title, description, tags, publish_at, category_id "27", synthetic_media true, made_for_kids false) following publish/metadata.md rules.

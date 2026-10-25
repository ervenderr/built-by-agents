You assemble and render a long 16:9 YouTube explainer from finished chapter sub-compositions. Work ONLY in /Users/ervenderr/Projects/youtube-os/videos/{slug}/. Do not change the narration or the chapter files except for obvious bugs you must report.

Inputs: `chapters.json` (id, title, start, duration of each chapter on the full timeline), `assets/narration.wav` (full narration, do not regenerate), `compositions/ch*.html` (one per chapter), `style.md`.
Method: read /Users/ervenderr/.claude/skills/hyperframes/SKILL.md and references (sub-composition mounting, format.md, spec.md). Scaffold if there is no index.html or hyperframes.json: HYPERFRAMES_SKIP_SKILLS=1 npx hyperframes init . --example blank --resolution landscape --non-interactive --skip-transcribe (keep existing files).
1. Write the root `index.html` (1920x1080): mount each chapter composition at its `start` with its `duration`, the narration audio from 0 (audio duration = narration length), a thin chapter-title lower-third at each chapter start, a small brand tag "BUILT BY AGENTS" (accent #00e5a0), and a 6-8 s end screen after the narration (title of the video, "subscribe" text, no fake UI). Root data-duration = narration end + 8 s. Use short crossfades between chapters, not cuts to black.
2. `npx hyperframes check --json` must be ok:true with 0 errors. Snapshot 10+ moments (every chapter boundary, the hook at frame 0, the end screen), look at them, fix problems.
3. Render: `npx hyperframes render -o out/{slug}.mp4` (create out/). Rendering may take many minutes: run it in the background if needed and poll.
4. Write README.md (topic, thesis, chapters with timestamps, voice: VoiceStudio BuiltByAgentsExplainer seed 42, what is unverified) and CREDITS.md.
Run tools/status.py {slug} rendering "<what>" at each step (python3 /Users/ervenderr/Projects/youtube-os/tools/status.py).
Reply with ONE line: DONE <duration seconds> check_errors=<n>.

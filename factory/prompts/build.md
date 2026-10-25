You build the animation for ONE YouTube Short. Work ONLY in /Users/ervenderr/Projects/youtube-os/videos/{slug}/. The factory already wrote `script.txt`, `assets/narration.wav` and `timings.json` (start and duration of every sentence, in seconds). Do not regenerate or change the narration.

Topic: {working_title}   Visual style: {style}   Angle: {angle}
{remix}
Visual retention: also read the animation/pacing rules in /Users/ervenderr/Projects/youtube-os/research/engagement-playbook.md and apply them (a visual change every few seconds in Shorts and every 20-30 s in long-form, concrete pictures and comparisons rather than diagrams of boxes, motion that explains).
Rules and method: read /Users/ervenderr/.claude/skills/hyperframes/SKILL.md and its references (types/vertical.md, format.md, runtimes.md, captions.md, motion.md; types/3d.md for 3d). Layout/contract template that passes check: /Users/ervenderr/Projects/youtube-os/videos/agent-loop/index.html. Other finished examples: videos/gradient-descent (Three.js), videos/whiteboard-nn, videos/prompt-journey, videos/ai-history, videos/recursion. Do NOT copy an existing video's look: use a visibly different layout and motion idea for this topic.
1. Scaffold if the folder has no index.html: HYPERFRAMES_SKIP_SKILLS=1 npx hyperframes init . --example blank --resolution portrait --non-interactive --skip-transcribe (run inside the folder; keep existing script.txt and assets).
2. Build index.html: 1080x1920; one scene or beat per sentence, timed from timings.json; burned-in captions, one per sentence with the key word highlighted; text inside y 168-1330, captions near y 1190; frame 0 shows the hook; dim colours contrast >= 3:1; moving objects never cover labels; the last line stays on screen >= 2 s (set root data-duration = narration end + 2 s, audio element duration = narration length); fromTo not from; one paused root timeline; brand tag "BUILT BY AGENTS" and accent #00e5a0. Label any illustrative number "ILLUSTRATIVE" on screen.
3. `npx hyperframes check --json` must be ok:true with 0 errors. Snapshot 6+ moments with `npx hyperframes snapshot`, look at the frames, fix problems.
4. Render: `npx hyperframes render -o out/{slug}.mp4` (create out/).
5. Write README.md (topic, script, voice: VoiceStudio BuiltByAgentsExplainer seed 42, what is unverified) and CREDITS.md (repo author remixed with URL, if any).
6. Run: python3 /Users/ervenderr/Projects/youtube-os/tools/status.py {slug} building "<what you are doing>" at each step.
Reply with ONE line: DONE <duration seconds> check_errors=<n>.

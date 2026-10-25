# Workflow: from topic to published video (Shorts and long-form)

```
 PLAN            SCRIPT              FACTS              VOICE            BUILD
 planner agent → script-writer  →   fact-checker   →   VoiceStudio  →   animation-builder
 picks topics    researches, writes  independent agent  profile          writes HyperFrames
 (checks what    script.txt +        tries to break      BuiltByAgentsExplainer    index.html, checks,
  exists, what   SOURCES.md          every claim;        seed 42, each    renders out/<slug>.mp4
  performed)     (opens real pages)  rewrite up to 2x    sentence verified
                                          │
   ┌──────────────────────────────────────┘
   ▼
 VERIFY  →  META  →  ⛔ YOU (review)  →  UPLOAD  →  TRACK
 transcribe  title,    watch it, y/N      private +     views feed back
 the render  description, (factory/       scheduled     into the planner
 vs script   tags       run.sh review)    (publishAt)
```

## Stages, owners and the artifact that proves each is done
| Stage | Who | Artifact (stage is skipped on re-run if present and fresh) |
|---|---|---|
| plan | `claude -p` (prompts/plan.md) | `videos/<slug>/topic.json` |
| script | `claude -p` (prompts/script.md) | `script.txt` (one sentence per line, 45-70 words), `SOURCES.md` (URL + quote per claim) |
| facts | independent `claude -p` (prompts/facts.md) | `facts.json` `{ok, issues[severity blocking/minor]}`; blocks only on WRONG/UNVERIFIED/material overclaim; script rewritten up to 2x |
| voice | `tools/shorts.py narrate --engine voicestudio --voice BuiltByAgentsExplainer` | `assets/narration.wav`, `timings.json` (start/duration per sentence) |
| build | `claude -p` (prompts/build.md) | `index.html` + `out/<slug>.mp4`; `hyperframes check` 0 errors |
| verify | `tools/shorts.py verify` | `.verified` (render audio transcript matches script, ratio >= 0.93, last words match) |
| meta | `claude -p` (prompts/meta.md) | `metadata.json` |
| review | **you** | `factory/run.sh review` plays the video, shows title/description/tags and the next schedule slot |
| upload | `tools/upload.py` | `publish/uploaded.json` ledger; video is private + scheduled |

## Rules the pipeline enforces
- **No upload without your approval.** Nothing leaves your machine before `review`.
- **Every claim sourced.** The script agent opens real pages; a different agent checks again.
- **Audio must match the script.** `verify` transcribes the finished video (catches missing/duplicated sentences).
- **One voice.** Profile `BuiltByAgentsExplainer` (VoiceStudio archetype "The Explainer": male, young adult, moderate pitch, British accent; seed 42), via the app's seeded `/generate` route. Pitch stays within ~5 Hz across videos.
- **Original content.** Every video needs its own script and point of view; vary the visual style; never post templated repeats (YouTube demonetizes mass-produced content at channel level).

## Schedule
2 Shorts per day at 09:00 and 21:00 Manila time (morning in the US/Canada), including weekends. `review` assigns the next free slot after the last scheduled video. Long-form (1 per day is the target) has no pipeline yet.

## Cost (estimates from the pilot, not guarantees)
About $2 per Short (script+facts ~$1.30, voice->meta ~$0.64 in the pilot), about 100-260k tokens. Every `claude -p` call has a spending cap (plan $1.5, script $2.5, facts $2.5, build $8, meta $1). The live view shows the running total.


## Long-form (16:9, `factory/run.sh long run`)
```
 OUTLINE -> SCRIPT -> FACTS -> VOICE -> BUILD -> VERIFY -> META -> YOU -> UPLOAD
 thesis,    per-chapter  independent  per-chapter  N chapter agents  render vs   title,        review  private +
 chapters,  files        checker,     narration,   in parallel +     script      timestamps,           scheduled
 sources    script/chNN  2 rewrites   concatenated stitch + render               thumbnail
```
| Stage | Artifact |
|---|---|
| outline | `outline.json` (thesis, promise, chapters with goal/claims/visual idea/word target, sources) |
| script | `script/chNN.txt` (one sentence per line), `script.txt` (joined), `SOURCES.md` |
| facts | `facts.json` (same blocking/minor rule as Shorts, per-chapter line numbers) |
| voice | `assets-vs/chNN/`, `chapters/chNN.timings.json`, `assets/narration.wav` (0.6 s gaps), `timings.json`, `chapters.json` |
| build | `compositions/chNN.html` (one agent per chapter, shared `style.md`), root `index.html`, `out/<slug>.mp4` |
| verify | `.verified` (`shorts.py verify` on the full render) |
| meta | `metadata.json` (chapter timestamps in the description, no #Shorts, `thumbnail`), `thumbnail.png` |
Measured: `how-neural-nets-learn` (3:56, 5 chapters) cost $3.88 and about 30-45 minutes. Long-form slot is 18:00 Manila (about 6 am US Eastern); Shorts keep 09:00 and 21:00.

## Making videos interesting (general audience)
Prompts follow `research/engagement-playbook.md` (15-rule checklist: hook about the subject, surprising sourced fact by second 30, name the wrong belief first, a "wait, really?" beat at least every 90 s, a visual for every claim within 2 s, a transfer line at the end) and topics come from `research/topics-broad.md`.

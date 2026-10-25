# The Sun Vanishes (long, 16:9)

**Topic:** What would happen if the Sun vanished.
**Thesis:** Light and gravity both travel at c, so for 8 min 20 s nothing changes: the sky stays bright and Earth keeps orbiting a Sun that is gone. Then both vanish at once and Earth flies off in a straight line at ~30 km/s.

## Chapters
| # | Start | Title |
|---|-------|-------|
| 01 | 0:00 | The Sun is gone. You wouldn't know. |
| 02 | 0:43 | Why the sky stays bright for 8 minutes |
| 03 | 1:36 | Gravity has a speed limit too |
| 04 | 2:34 | What Earth does at the 8:20 mark |
| 05 | 3:28 | News can't outrun light |

Narration ends 4:02; end screen to 4:10 (250.11 s).

## Voice
VoiceStudio BuiltByAgentsExplainer, seed 42.

## Unverified / needs reword (see facts.json, SOURCES.md)
- "Many people assume we'd notice at once": no source.
- GW170817 gamma-ray delay quoted as ~1.7 s; measured 1.74 ± 0.05 s.
- "Humans freeze within weeks": sources say surface below freezing in days to a week; not directly sourced.
- Train analogy: 100 km/h vehicle is not a bullet train.
- GW170817 detected by three detectors, narration says two.
- "Other observations disagree" implies false balance; only a few papers question it.
- Derived, not sourced: 29.78 km/s x 500 s ~ 14,890 km; 150e6 km at 100 km/h ~ 171 years.
- Narration was left unchanged, so these lines still need a script fix before publishing.

## Build
`npx hyperframes render -o out/sun-vanishes.mp4`. Fixed one bug in `compositions/ch03.html`: a `letterSpacing` tween (lint error) replaced by `scaleX`.

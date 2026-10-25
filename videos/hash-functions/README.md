# Hash Functions (YouTube Short)

Topic: hash functions. Angle: any input, any size in; fixed-length fingerprint out; one changed character scrambles it.
Visual style: diagram (hash-machine rows, 256 counter, real SHA-256 digests, avalanche grid, fingerprint compare).

## Script
See `script.txt` (6 sentences, timed in `timings.json`).

## Voice
VoiceStudio BuiltByAgents, seed 42. Narration in `assets/narration.wav` (24.36 s), not regenerated.

## Build
`npx hyperframes check --json` (ok, 0 errors, warnings: dense caption track, hex reading time), render to `out/hash-functions.mp4` (26.4 s).

## Unverified
- Digests shown for "hello"/"hellp" and the 6-char prefixes for "hi" and the two placeholder inputs are real SHA-256 values (computed with Python hashlib); the 63/64 character difference was computed, not estimated.
- The "a whole book" / "a 4 GB video file" rows show prefixes of SHA-256 of stand-in bytes, not of real files (illustrative).
- Avalanche grid is decorative, labelled ILLUSTRATIVE.
- Facts check (facts.json) flagged wording issues in the script; not re-reviewed here.

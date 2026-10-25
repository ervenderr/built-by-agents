Topic: "One forward pass in 3D", 1080x1920, 18.5 s, HyperFrames + Three.js (seek-driven, seeded PRNG, no timers).
Script: A forward pass is one trip through a neural network. Numbers flow in at the input layer. Those can be pixels, or words turned into numbers. Each layer mixes them with weights, then usually applies a nonlinearity. No learning happens here, the weights stay fixed. The last layer produces the answer.
Voice: VoiceStudio profile BuiltByAgentsExplainer, The Explainer design voice, seed 42 (via tools/shorts.py narrate; previous render kept as out/forward-pass-3d.documentarian.mp4).
Render: npx hyperframes render -o out/forward-pass-3d.mp4 (check: npx hyperframes check --json).
Credits in CREDITS.md, facts in SOURCES.md.

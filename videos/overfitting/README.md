# Overfitting (Whiteboard in 20 Seconds)

Topic: What Is Overfitting? A model that memorizes its training data fails on new data; the whiteboard curve shows why.

## Script
Your model can ace every training example and still fail in real life.
That is overfitting.
It means the model memorizes the training set so closely that it fails on new data.
On the whiteboard, a wiggly curve hits every dot perfectly.
But a simple line would likely predict new points better.
So watch validation loss, not just training loss.

Voice: VoiceStudio BuiltByAgents, seed 42.
Render: `npx hyperframes render -o out/overfitting.mp4` (1080x1920, 21.59 s).

## Unverified
- All data points and loss curves are schematic and marked ILLUSTRATIVE; no real model was trained.
- "Simple line likely better" is a general rule of thumb, not shown for any specific dataset.
- Claims are checked in SOURCES.md / facts.json, not re-checked here.
- The check passes with a GSAP CDN link; one earlier check run failed to fetch it (network), the rerun passed.

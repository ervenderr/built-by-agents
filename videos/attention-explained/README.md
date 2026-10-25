# attention-explained
Topic: What Is Attention in an LLM? Explained in 20 Seconds (data-bars style, 1080x1920, ~20.9 s).

## Script
How does an AI know what a word means?
It uses attention, where each word looks at the other words around it.
Each word gives the other words a score.
Then softmax turns those scores into weights that are positive and add up to one.
A bigger weight means that word matters more here.
The word's new meaning is a weighted sum of all of them.

## Voice
VoiceStudio BuiltByAgents, seed 42 (assets/narration.wav, unchanged).

## Unverified
- All scores/weights (ANIMAL 75%, TIRED 17%, ...) are made up for illustration and labelled ILLUSTRATIVE on screen; they are not from a real model.
- Example sentence ("animal ... it ... tired") is a teaching example, not real attention output.
- Facts per SOURCES.md / facts.json from the factory.

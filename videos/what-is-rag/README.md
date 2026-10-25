# What Is RAG? How AI Looks Things Up

Angle: retrieval-augmented generation fetches relevant documents first, then the model answers using them.
Style: diagram (vertical flow: question → knowledge base → model → answer with source).

## Script
Most AI answers come from memory, but RAG lets the model open the book first.
RAG stands for retrieval-augmented generation.
Your question first triggers a search of an outside knowledge base.
Then the question and the relevant information are both given to the model.
It answers using them, so new facts need no retraining.
It can even cite sources, which beats guessing from memory.

## Voice
VoiceStudio BuiltByAgents, seed 42.

## Build
`npx hyperframes render -o out/what-is-rag.mp4` (1080x1920, 23.35 s: narration 21.35 s + 2 s hold).

## Unverified
- Facts are as checked in facts.json / SOURCES.md; nothing was re-verified during the animation build.
- The "refund policy" question, DOC 2 / DOC 4 and the NEW doc are illustrative (labelled ILLUSTRATIVE EXAMPLE on screen).
- Caption timing is per sentence from timings.json; the RETRIEVAL/AUGMENTED/GENERATION highlights are timed by eye, not word-aligned.

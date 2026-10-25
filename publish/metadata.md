# Shorts metadata: batch 1 (8 animated Shorts)

## Rules for every batch (reuse)
- Title: max ~70 chars, states the topic and the promise, no fake clickbait, no ALL CAPS. Put the concept in the first 40 characters.
- Description: line 1 = what the viewer learns; line 2 = what is illustrative or uncertain; credit line for the repo author; disclosure line; 2-3 hashtags (#Shorts is added automatically for vertical under 3 min, add it anyway).
- Disclosure line (every video): "Narration is a synthetic voice (Kokoro). Animation is written as code." Also answer YouTube's altered/synthetic content question in Studio according to its current wording.
- Never post a video until: (1) a human has watched it, (2) the rendered audio transcript matches the script, (3) every fact has a URL in its `SOURCES.md`.
- Upload by hand in YouTube Studio (clipper is not used for this channel). Default audience: not made for kids.
- Template for the next batch: ask Claude "write title, description, tags for videos/<name> from its README.md, SOURCES.md and CREDITS.md using publish/metadata.md rules". If you prefer an agent, run it in a new session so `.claude/agents/marketing-video-optimization-specialist` loads.

## Posting order (4/week, 21:00 Manila = morning in the US/Canada)
| # | Date (Manila) | Video | Gate before posting |
|---|---|---|---|
| 1 | Mon Oct 26 21:00 | agent-loop | watch it |
| 2 | Wed Oct 28 21:00 | prompt-journey | watch it; confirm the "Attention Is All You Need" citation |
| 3 | Thu Oct 29 21:00 | whiteboard-nn | watch it; open the second source (Towards Data Science) or drop it |
| 4 | Sat Oct 31 21:00 | forward-pass-3d | watch it; open its sources (they came from search results only) |
| 5 | Mon Nov 2 21:00 | recursion | watch it |
| 6 | Wed Nov 4 21:00 | next-word | confirm the "sampling" claim against a source |
| 7 | Thu Nov 5 21:00 | gradient-descent | confirm "overshoot" wording against a source |
| 8 | Sat Nov 7 21:00 | ai-history | verify each date again, replace Wikipedia-only ChatGPT date, fix "named the field" wording, check the 1.2x voice speed |

Why this order: the most self-evidently correct explainers go first; the ones with open fact questions go last, giving time to verify.

---

## 1. agent-loop
**Title:** AI Agents Are Just a Loop (Explained in 20 Seconds)
**Description:**
An AI agent isn't magic: it's a model, instructions, tools and memory running in a loop, with a step limit so it can't run forever.

Animation idea inspired by the strict "one draw(t), deterministic" prompt style in yihui-dev/awesome-opus5-5-videos. Narration is a synthetic voice (Kokoro). Animation is written as code.

#Shorts #AIagents #AI
**Tags:** ai agents, how ai agents work, agent loop, llm tools, tool calling, ai explained, artificial intelligence

## 2. prompt-journey
**Title:** What Happens to Your Prompt Before an AI Replies
**Description:**
Your prompt is chopped into tokens, turned into numbers, passed through transformer layers, and the reply is written one token at a time.

The tokens, numbers and layers shown are illustrative. Inspired by @AstroTheWizard's whimsical "journey of photons" explainer prompt (yihui-dev/awesome-opus5-5-videos). Narration is a synthetic voice (Kokoro). Animation is written as code.

#Shorts #LLM #AI
**Tags:** how chatgpt works, tokens, embeddings, transformer, attention, llm explained, ai explained

## 3. whiteboard-nn
**Title:** What Is a Neural Network? (Whiteboard in 23 Seconds)
**Description:**
A neural network is layers of simple units joined by weights. It learns by comparing its output with the right answer and nudging the weights to shrink the error.

Inspired by @tak3sh8's hand-drawn whiteboard animation prompt (yihui-dev/awesome-opus5-5-videos). Narration is a synthetic voice (Kokoro). Animation is written as code.

#Shorts #NeuralNetworks #MachineLearning
**Tags:** neural network explained, what is a neural network, weights, machine learning basics, deep learning, whiteboard

## 4. forward-pass-3d
**Title:** One Forward Pass Through a Neural Network (3D)
**Description:**
A forward pass is one trip through a network: numbers go in, each layer mixes them with weights and applies a nonlinearity, and the last layer gives the answer. No learning happens in a forward pass.

Inspired by @mdaman010's AI data centre and @lukasersil's showreel prompts (yihui-dev/awesome-opus5-5-videos). Narration is a synthetic voice (Kokoro). Animation is written as code (Three.js).

#Shorts #NeuralNetworks #AI
**Tags:** forward pass, neural network 3d, deep learning, activation function, weights, ai explained

## 5. recursion
**Title:** Recursion in 5 Styles (Still Confused? See: Recursion)
**Description:**
Recursion is a function solving a problem by calling itself on a smaller version, and it needs a base case to stop. Factorial of 3 waits for 2, which waits for 1, then the answers come back up: 6.

Inspired by @emollick's "explain recursion in radically different styles" prompt (yihui-dev/awesome-opus5-5-videos). Narration is a synthetic voice (Kokoro). Animation is written as code.

#Shorts #Recursion #Programming
**Tags:** recursion, recursion explained, base case, factorial, programming basics, computer science

## 6. next-word
**Title:** How an LLM Picks the Next Word
**Description:**
A language model scores every possible next token, turns the scores into probabilities, samples one, and temperature decides how adventurous that pick is.

The probabilities shown are illustrative, not from a real model. Inspired by the strict-structure prompts of @verbove, @twoclipping and @__morse and by @emollick (yihui-dev/awesome-opus5-5-videos). Narration is a synthetic voice (Kokoro). Animation is written as code.

#Shorts #LLM #AI
**Tags:** llm temperature, next token prediction, how llms work, softmax, sampling, ai explained

## 7. gradient-descent
**Title:** Gradient Descent in 20 Seconds (3D)
**Description:**
A model learns by rolling downhill: parameters are its settings, the loss measures how wrong it is, the slope shows which way is down, and the learning rate sets the step size. Too big a step and it overshoots the bottom.

Inspired by @anirockshady's gradient-descent 3D animation prompt (yihui-dev/awesome-opus5-5-videos). Narration is a synthetic voice (Kokoro). Animation is written as code (Three.js).

#Shorts #MachineLearning #GradientDescent
**Tags:** gradient descent, learning rate, loss function, machine learning, optimization, 3d animation

## 8. ai-history
**Title:** AI History in 30 Seconds: 5 Moments That Mattered
**Description:**
Dartmouth 1956, Deep Blue 1997, AlexNet 2012, the Transformer 2017, ChatGPT 2022: five milestones in AI. Sources are listed in the project's SOURCES.md.

Inspired by @kloss_xyz's "key moments in the history of AI" prompt (yihui-dev/awesome-opus5-5-videos). Narration is a synthetic voice (Kokoro). Animation is written as code.

#Shorts #AIHistory #AI
**Tags:** history of ai, dartmouth workshop, deep blue, alexnet, transformer, chatgpt, ai timeline

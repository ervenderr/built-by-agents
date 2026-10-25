# Engagement playbook: animated explainers for a general audience

Researched 2026-10-25. Tags: [V] = page opened and read this session; [S] = only search-result snippets or secondary summary (treat as weak); [M] = from model memory, NOT verified; [P] = pattern observed from YouTube search results scraped this session (titles/views are real, the reading of "why it works" is my inference).

## 1. What YouTube itself says

- Retention report: "Intro retention" = share of viewers still watching after the first 30 seconds. High means the opening matched the title and thumbnail. YouTube's advice: align thumbnail/title with the content and experiment with the first 30 s. [V] https://support.google.com/youtube/answer/9314415
- Same page: flat line = watched start to finish; spikes = watched/rewatched/shared (or confusing, so check which); dips = skipped or left; "Top moments" late in a video -> move compelling content earlier, because "audiences shrink over a video's length". Typical retention compares against your 10 latest videos of similar length. [V] same URL
- Impressions CTR: half of all channels/videos sit between 2% and 10%. High-impression placements (Home) lower CTR; new or <100-view videos fall outside the range more. Don't judge right after upload; don't test multiple thumbnails on one video. [V] https://support.google.com/youtube/answer/7628154
- Same page: "Avoid clickbait thumbnails or titles"; the tell is high CTR + low average view duration + lower-than-expected impressions. YouTube is more likely to recommend a video when it is relevant and average view duration suggests viewers find it interesting. [V] same URL
- Recommendations use viewing behaviour, likes/dislikes, subscriptions and satisfaction-survey feedback, plus channel quality. Page does NOT name CTR or watch time. [V] https://www.youtube.com/howyoutubeworks/product-features/recommendations/
- Thumbnails: 16:9, up to 3840x2160, JPG/PNG, 2 MB limit on mobile. Shorts thumbnails 9:16. [V] https://support.google.com/youtube/answer/72431
- Shorts "viewed vs swiped away" (feed-level hook metric): only third-party descriptions found; the official page URL I tried 404'd. Benchmarks like "75-80% viewed" are third-party, not YouTube. [S] https://buffer.com/resources/the-creators-guide-to-youtube-shorts-analytics
- Not found: any official YouTube number for ideal video length or ideal first-30-s retention. Do not cite one.

## 2. Titles and thumbnails that earn the click honestly

Real titles from YouTube search results (view counts as scraped 2026-10-25) [P]:

| Pattern | Example (channel, views) |
|---|---|
| Premise contradicts common belief | "Why all world maps are wrong" (Vox, 23.8M); "Leap Years Don't Happen Every 4 Years" (CGP Grey, 7.5M) |
| Hypothetical with a physical answer | "What If The Sun Disappeared?" (Vsauce, 20.9M) |
| Everyday object, unexpected depth | "How The Internet Travels Across Oceans" (VISION, 11.9M); "How a Microwave Oven Works" (engineerguy, 5.4M) |
| Puzzle everyone argued about | "What Colour Is This Dress? (SOLVED with SCIENCE)" (AsapSCIENCE, 29.9M) |
| Extreme first-person proof | "I built a QR code with my bare hands to see how it works" (Veritasium, 9.7M) |
| Short question, short video | "Why is it Dark at Night?" (minutephysics, 3:53, 4.7M) |

Rules drawn from this:
- Title states a question or a contradiction the viewer already half-holds; the video must resolve it. Veritasium's clickbait video argues nearly any title uses the curiosity gap [S: search summary; the official page https://www.veritasium.com/videos/2021/8/17/we-need-to-talk-about-clickbait only says "The title and thumbnail play a huge role in a video's success or failure" [V]].
- "Double barrel": title and thumbnail should add tension to each other, not repeat each other. Source is a LinkedIn summary of a Veritasium interview [S, unverified]; treat as a heuristic.
- Honest test (from YouTube's own CTR page): if the video can't pay the promise off in the first third, the title is clickbait and average view duration will expose it.
- Thumbnail: one visual idea, readable at phone size, 3-4 words max, no faces needed (faceless channel). Contrast the "expected" and "actual" (e.g. Greenland vs Africa size). [M/inference]
- Public data on CTR by style is third-party only; I could not verify any "ideal CTR" beyond YouTube's 2-10% median band.

## 3. First 30 seconds: hook types (each must be tested against the title promise)

1. Wrong-belief flip: state what everyone believes, then say it is false. Muller's research: viewers with a misconception tune out explanations unless the misconception is stated first, then refuted. [V] https://www.creatorhandbook.net/inside-veritasium-an-interview-with-dr-derek-muller-12ad2351a4b3/
   Draft: "Planes stay up because air above the wing travels faster to meet air below. That's a myth, and NASA says so."
2. Impossible number: open on a figure the viewer can't square. Draft: "Every GPS satellite clock runs 38 millionths of a second a day fast. Ignore that and your map drifts." (38 µs/day from https://www.astronomy.ohio-state.edu/pogge.1/Ast162/Unit5/gps [V])
3. Conundrum / question to follow (Muller: offer "an interesting conundrum, or an interesting problem or question" and bring people along). [V] same creatorhandbook URL
4. Stakes in one sentence: what is lost if the thing fails (bridge falls, payment fails, map lies).
5. Cold-open scene: drop into the moment (a bridge twisting, a box lifted onto a ship) and explain after 10 s.
6. Promise + proof: "In 4 minutes you'll see why X; by the end you can predict Y."
- Do not: start with a channel intro, a logo sting, "hey guys", a subscribe ask, or a long definition. YouTube defines intro retention at 30 s, so anything not about the video's question in that window costs retention. [V reasoning from the retention page]

## 4. Storytelling devices

- Curiosity gap: Loewenstein's information-gap theory says curiosity comes from attention focused on a gap in knowledge; gaps that are too big or too small don't hold attention. Open with something the viewer partly knows. [S: abstract and secondary summaries only] https://stafforini.com/works/loewenstein-1994-psychology-curiosity-review/
- Counter-intuitive fact as the spine: Veritasium (usually addresses "counter-intuitive concepts") and CGP Grey ("often aimed at debunking common misconceptions") are built this way. [V] https://en.wikipedia.org/wiki/Veritasium , https://en.wikipedia.org/wiki/CGP_Grey
- Character to follow: CGP Grey uses a stick-figure avatar and never shows his face [V]; 3Blue1Brown gives math cartoon characters and treats the solution's "climax" as a payoff [V] https://www.stanforddaily.com/2020/01/24/3blue1brown-creator-grant-sanderson-15-talks-engaging-with-math-using-stories-and-visuals . Use one recurring object or mascot per series.
- Visuals first, meaning second: Sanderson says showing the visual then articulating it gives viewers "a sense of ownership". [V] same Stanford URL
- "Wait, really?" beats: schedule one every 60-90 s: a surprising number, a reversal, or a visual that contradicts the narration's first guess. (My heuristic [M]; no source gives a canonical interval.)
- Open loops: ask a question early, answer it late, and plant a smaller question before answering each one. A "stakes / big question / head fake / rehook" loop appears in third-party guides, not attributed to any named channel. [S] https://joyspace.ai/open-loop-technique-force-viewers-watch-end
- Close with a transfer: one thing the viewer can now predict or notice in daily life (Johnny Harris frames storytelling as "how you invite others to care"). [V session blurb] https://www.adobe.com/max/2025/sessions/scrappy-smart-and-human-the-future-of-storytelling-os558.html

## 5. Pacing and pattern interrupts for 5-10 minute videos

Evidence is thin; be honest about it:
- Guo, Kim and Rubin (2014, ACM L@S), 6.9M watch sessions on edX: median engagement time was at most 6 minutes regardless of video length; shorter videos far more engaging; fast, enthusiastic speakers beat slow ones; Khan-style drawing with motion beat static slides; informal beats polished studio. Recommendation: segment into chunks under 6 minutes. [V, read PDF] https://dl.acm.org/doi/10.1145/2556325.2566239 (MIT copy: https://up.csail.mit.edu/other-pubs/las2014-pguo-engagement.pdf). Caveat: course videos, not entertainment explainers.
- Implication [inference]: structure a 8-10 min video as 2-3 "chapters" of 3-4 min, each with its own mini-question and mini-payoff, so each chapter is a fresh entry point.
- Pattern interrupt toolbox (change at least one of these every 8-12 s): camera/zoom move, scene change, scale jump (zoom from a coin to the planet), new color accent, on-screen number counting, sound hit, narrator tone shift, a one-word text slam. Intervals are my heuristic [M].
- Use YouTube's own diagnostics after publishing: read dips and spikes in the retention report; if the "Top moment" is late, move that content earlier next time. [V]
- Speaking speed: Guo found faster speaking correlated with engagement [V]; synthetic narrator should be tuned to energetic but clear, not slowed down.

## 6. What the named channels demonstrably do

- Kurzgesagt: research from books and papers, expert consults, a "sourcesheet" per video, scripts "can take about a dozen drafts", narrator's voiceover sets animation timing, original soundtrack per video. [V] https://kurzgesagt.org/youtube/ . Flat minimalist visuals, some 3D; ~25.6M subs; coronavirus video 89M+ views. [V] https://en.wikipedia.org/wiki/Kurzgesagt . Cautionary: removed two 2015 videos in 2019 for weak sourcing and re-did a 2024 exercise video after criticism of oversimplification. [V same]. Takeaway: fact-check before publishing; a faceless channel's only credibility is its sources.
- Veritasium: counter-intuitive science, public interviews to find misconceptions, experiments and expert interviews. [V Wikipedia]
- TED-Ed: 3-5 min lessons from teacher + scriptwriter + animator + voice actor. [S] https://www.cartoonbrew.com/biz/buzzco-creates-animation-for-ted%e2%80%99s-ted-ed-initiative-61854.html
- CGP Grey: narration over animation plus stock footage; stick-figure avatar; influenced by Zero Punctuation's style. [V]
- Wendover / Half as Interesting: one little-known logistics/economics topic per video, "educational entertainment", witty. [V] https://en.wikipedia.org/wiki/Wendover_Productions . No script-process interview found.
- 3Blue1Brown: manim custom animation library; emotion, wonder and "story and intrinsic delight" over usefulness; dense videos meant to be paused. [V Stanford Daily]
- Johnny Harris / Vox Borders: fast visually driven history/geopolitics; critics say it oversimplifies and omits context. [V] https://en.wikipedia.org/wiki/Johnny_Harris_(journalist)
- Fireship-style (fast code explainers): NOT researched this session. [unverified]
- Animation style and retention: I found no study that ranks animation styles by retention. The only measurable evidence is Guo's "motion and continuous visual flow" finding. Flat vector + motion graphics is what Kurzgesagt, CGP Grey and 3b1b converged on, and it is what code rendering does cheaply. [inference]

## 7. Rules for Built by Agents (general audience)

- Topic must have a visible mechanism (something that moves, flows, grows, or scales) so animation adds information.
- Avoid claims that need a medical, political or "experts disagree" caveat; where science is contested (e.g. zebra stripes, bird navigation), say "the best-supported explanation" on screen.

## CHECKLIST (for LLM script writer and LLM animation builder)

1. The title is a question or contradiction whose answer is shown by minute 1 of a 5-minute video (or by the 25% mark of a longer one), and the script contains a line that visibly resolves it.
2. The first sentence of the script is about the subject (no greeting, channel name or definition) and is under 20 words.
3. By second 30, the script has stated a surprising specific fact (a number, a reversal or a myth being flipped) that is traceable to a named source.
4. The script names the common wrong belief before correcting it, whenever the topic has one.
5. Every video has exactly one central question, stated in one sentence in the script and on screen in the first 30 seconds.
6. A "wait, really?" beat (new number, reversal or contradicting visual) appears at least every 90 seconds, and each is listed in the script's beat sheet.
7. Videos over 6 minutes are split into labelled chapters, each opening with its own sub-question and ending with a mini-payoff.
8. No scene holds the same composition for more than 10 seconds; each scene change alters at least one of camera, scale, color accent or object motion.
9. Every narrated claim has a matching on-screen visual (object, diagram, number or label) within 2 seconds, and nothing on screen is decorative only.
10. Numbers on screen animate (count, scale or compare) instead of appearing as static text, and comparisons use a physical size or ratio the viewer can picture.
11. A recurring character or object (one per series) appears in the opening and the closing scene to give the viewer someone to follow.
12. Narration runs at an energetic pace (no artificial slow-down) and every sentence is under 25 words.
13. Every factual claim has an entry in a sources list with a URL, and anything unverified is cut or phrased as uncertain.
14. The last 20 seconds give a transfer line (what the viewer can now predict or spot in daily life) and either a teaser for a specific next video or nothing, never a generic subscribe plea before the payoff.
15. The thumbnail has one visual idea, at most four words, adds tension to the title rather than repeating it, and is checked at 160 px width.

## Open gaps

- No first-party data from this channel yet: after 5 videos, compare intro retention (30 s) and average view duration with the 10-video typical-retention band in Studio, and revise rules 1-8.
- Not verified: Shorts hook benchmarks, "double barrel" claim, ideal chapter length, pattern-interrupt interval.

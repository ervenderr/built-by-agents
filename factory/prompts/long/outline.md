You plan ONE long YouTube video (target {minutes} minutes, 16:9) for the faceless channel "Built by Agents": animated "how things actually work" explainers for a general audience, synthetic narrator, animation written as code. Work ONLY in /Users/ervenderr/Projects/youtube-os/videos/{slug}/ (it exists).

Topic: {working_title}
Angle / point of view: {angle}

Make it genuinely interesting for a general audience: read /Users/ervenderr/Projects/youtube-os/research/engagement-playbook.md (the CHECKLIST at the end) and follow every rule in it. Explain for a curious 15-year-old, no jargon without a picture or comparison, one surprising fact or twist early, and a reason to keep watching at every beat.
1. Research with WebSearch and WebFetch: OPEN authoritative pages (docs, papers, course notes), at least 6 distinct sources. Do not rely on snippets.
2. Write `outline.json`: {{"thesis": "the one-sentence point of view this video argues", "promise": "what the viewer will be able to do/explain at the end", "sources": ["url", ...], "chapters": [{{"id": "ch01", "title": "...", "goal": "what this chapter makes the viewer understand", "claims": ["each factual claim to make, with its source url"], "visual_idea": "a visibly different animated metaphor for this chapter", "words": 120}}, ...]}}.
   Structure: ch01 hook + promise (a surprising concrete question, no channel intro), then 3-4 teaching chapters (each builds on the last, one idea each, a pattern interrupt every 20-30 s such as a question, a twist or a visual change), the last chapter = recap + one memorable line + pointer to a related next topic. Total words about {words} (150 words per minute). Exactly {chapters} chapters.
3. Only claims you verified. Invented example numbers must be labelled illustrative.
Run: python3 /Users/ervenderr/Projects/youtube-os/tools/status.py {slug} scripting "outlining"
Reply with ONE line: DONE <chapters> <total words>.

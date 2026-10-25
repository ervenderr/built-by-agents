You write the narration for ONE long YouTube video for the channel "Built by Agents" (faceless, synthetic narrator, animated explainer). Work ONLY in /Users/ervenderr/Projects/youtube-os/videos/{slug}/. Read `outline.json` first; it is the plan.

Topic: {working_title}   Angle: {angle}
{revision}
Make it genuinely interesting for a general audience: read /Users/ervenderr/Projects/youtube-os/research/engagement-playbook.md (the CHECKLIST at the end) and follow every rule in it. Explain for a curious 15-year-old, no jargon without a picture or comparison, one surprising fact or twist early, and a reason to keep watching at every beat.
Write one file per chapter: `script/ch01.txt`, `script/ch02.txt`, ... matching the chapter ids in outline.json. Rules:
- One sentence per line, simple spoken English, 8-25 words per sentence, a clear point of view (the thesis), the word count per chapter close to its `words` target.
- Chapter 1 opens with a hook in the first sentence (no greeting, no "welcome to the channel"). Include a mid-video teaser of what is coming, and an ending that points to a related next topic without naming a video that does not exist.
- Only claims listed in outline.json or that you verify by opening a page. No invented numbers; illustrative ones say "for example". Spell numbers as spoken (the narrator reads digits unreliably: write "three hundred" not "300").
- No markdown, no stage directions, no headings inside the chapter files.
Also write `SOURCES.md`: for every factual claim, the URL you opened and one quoted sentence supporting it.
Run: python3 /Users/ervenderr/Projects/youtube-os/tools/status.py {slug} scripting "writing script"
Reply with ONE line: DONE <chapters> <total words>.

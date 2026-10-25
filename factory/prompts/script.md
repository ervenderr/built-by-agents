You write the script for ONE YouTube Short for the channel "Built by Agents" (faceless, synthetic narrator, animated explainer). Work ONLY in /Users/ervenderr/Projects/youtube-os/videos/{slug}/ (it exists).

Topic: {working_title}
Angle: {angle}
{revision}
Make it genuinely interesting for a general audience: read /Users/ervenderr/Projects/youtube-os/research/engagement-playbook.md (the CHECKLIST at the end) and follow every rule in it. Explain for a curious 15-year-old, no jargon without a picture or comparison, one surprising fact or twist early, and a reason to keep watching at every beat.
Do this:
1. Research the topic: use WebSearch and WebFetch to OPEN authoritative pages (official docs, papers, university course notes). Do not rely on search snippets.
2. Write `script.txt`: one sentence per line, 5-7 lines, 45-70 words total, simple spoken English, a clear point of view, a hook in the first line. Only claims you verified. No invented numbers; if an example number is illustrative, say "for example" in the sentence.
3. Write `SOURCES.md`: for every factual claim, the URL you opened and one quoted sentence supporting it.
4. Run: python3 /Users/ervenderr/Projects/youtube-os/tools/status.py {slug} scripting "writing script"
Reply with ONE line: DONE <number of sentences> <word count>.

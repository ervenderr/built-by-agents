# Sources

1. "It reads chunks of text called tokens" (lines 2, 6)
   - https://github.com/karpathy/minbpe/blob/master/lecture.md (opened)
   - "work not on a character level, but on character chunk level."

2. Common words stay whole, rare words split (line 3)
   - https://huggingface.co/docs/transformers/tokenizer_summary (opened)
   - "Common words stay intact as single tokens, and rare or unknown words decompose into subwords."

3. annoyingly example (line 4)
   - https://huggingface.co/docs/transformers/tokenizer_summary (opened)
   - "For instance, `annoyingly` might be split into `[\"annoying\", \"ly\"]` or `[\"annoy\", \"ing\", \"ly\"]` depending on the vocabulary."

4. Spelling mistakes trace to tokenization (lines 5, 6)
   - https://github.com/karpathy/minbpe/blob/master/lecture.md (opened; Karpathy's lecture notes)
   - "Why can't LLM spell words? Tokenization."
   - "A lot of the issues that may look like issues with the neural network architecture actually trace back to tokenization."

Line 1 is framing, no factual claim beyond the above.
Note: WebFetch returned paraphrased/extracted text, not raw page; quotes are as returned.

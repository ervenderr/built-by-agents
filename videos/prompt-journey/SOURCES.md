# Sources
- Tokenization: text is split into tokens (words, subwords, characters; BPE/Unigram/WordPiece) before the model sees it. Hugging Face docs, "Tokenization algorithms": https://huggingface.co/docs/transformers/en/tokenizer_summary
- Transformer architecture built on attention: Vaswani et al., "Attention Is All You Need" (2017): https://arxiv.org/abs/1706.03762 (also describes learned embeddings turning tokens into vectors, section 3.4; the abstract page was fetched, section 3.4 is from memory of the paper, not re-fetched).
- Next-token generation, one token at a time, each generated token feeds the next step; scores for the next token then greedy/sampled choice: Hugging Face docs, "Text generation": https://huggingface.co/docs/transformers/en/llm_tutorial
- No numbers in the video are real model data. Token split, vectors, layer count, attention weights, candidate words and the reply are all labelled ILLUSTRATIVE on screen.

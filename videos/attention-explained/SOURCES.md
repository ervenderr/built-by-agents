# Sources

1. Line 2 (each word looks at other words)
   - https://jalammar.github.io/illustrated-transformer/ (opened)
   - "self attention allows it to look at other positions in the input sequence for clues"
   - https://web.stanford.edu/~jurafsky/slp3/9.pdf (opened, text extracted): "In processing each token, the model attends to all inputs, both before and after the current one."
2. Line 3 (scores)
   - Same Alammar page: "The score is calculated by taking the dot product of the query vector with the key vector of the respective word"
3. Line 4 (softmax weights)
   - Same Alammar page: "Softmax normalizes the scores so they're all positive and add up to 1."
4. Line 5 (bigger weight matters more)
   - Same Alammar page: "This softmax score determines how much each word will be expressed at this position."
5. Line 6 (weighted sum)
   - Same Alammar page: "The sixth step is to sum up the weighted value vectors."
6. Attention is central to the Transformer
   - https://arxiv.org/abs/1706.03762 (opened): "...the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely."

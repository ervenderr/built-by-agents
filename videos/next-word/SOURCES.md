# Sources
- Mistral, "Concept deep dive: sampling temperature" https://docs.mistral.ai/resources/cookbooks/concept-deep-dive-sampling-temperature (fetched): logits -> softmax -> probabilities; higher temperature flattens, lower sharpens. Does not itself describe the sampling step.
- Machine Learning Mastery, "The Statistics of Token Selection" https://machinelearningmastery.com/the-statistics-of-token-selection-logits-temperature-and-top-p-walkthrough/ (WebSearch summary only, page not fetched): next token is sampled from the distribution, not always the top one.
- Also seen in search results: aman.ai token-sampling primer, Towards Data Science temperature article.
- All on-screen numbers are illustrative, labelled ILLUSTRATIVE; computed as softmax(z/T) from made-up scores. No real model output or statistics.

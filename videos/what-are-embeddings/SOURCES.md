# Sources

1. "Embedding is a list of numbers / point in space" (script lines 1-2)
   - https://web.stanford.edu/~jurafsky/slp3/5.pdf (Jurafsky & Martin, Speech and Language Processing, ch. 5, opened; text extracted)
   - "The idea of vector semantics is to represent a word as a point in a multidimensional semantic space that is derived (in different ways we'll see) from the distributions of word neighbors. Vectors for representing words are called embeddings."
   - https://developers.openai.com/api/docs/guides/embeddings (opened)
   - "An embedding is a vector (list) of floating point numbers."

2. Similar meanings are close together; cat/dog (line 3)
   - https://web.stanford.edu/~jurafsky/slp3/5.pdf
   - "...showing that words with similar meanings are nearby in space." (Fig. 5.1)
   - "It should tell us that some words have similar meanings (cat is similar to dog)..."

3. Different meanings land far apart; distance measures meaning/relatedness (lines 4-5)
   - https://developers.openai.com/api/docs/guides/embeddings
   - "The distance between two vectors measures their relatedness." and "Small distances suggest high relatedness and large distances suggest low relatedness."

4. Search, clustering, recommendations (line 5)
   - https://developers.openai.com/api/docs/guides/embeddings
   - Lists use cases: Search ("results are ranked by relevance to a query string"), Clustering ("text strings are grouped by similarity"), Recommendations ("items with related text strings are recommended").

5. Word meaning as coordinates (line 6, framing)
   - https://web.stanford.edu/~jurafsky/slp3/5.pdf
   - "This revolutionary idea that word meaning could be represented as a point in space..."

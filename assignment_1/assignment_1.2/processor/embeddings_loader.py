# embeddings_loader.py

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

class EmbeddingHandler:
    def __init__(self, corpus):
        self.corpus = corpus
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(corpus)
        self.word_to_index = self.vectorizer.vocabulary_

        self.glove_vectors = {}
        self.load_glove()

    def load_glove(self, path="models/glove.6B.100d.txt"):
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                values = line.split()
                word = values[0]
                vector = np.array(values[1:], dtype='float32')
                self.glove_vectors[word] = vector

    def get_vector(self, word):
        if word in self.glove_vectors:
            return self.glove_vectors[word]
        elif word in self.word_to_index:
            idx = self.word_to_index[word]
            return self.tfidf_matrix[:, idx].toarray().flatten()
        else:
            return None

    def get_nearest_neighbors(self, word, top_n=5):
        from sklearn.metrics.pairwise import cosine_similarity

        vec = self.get_vector(word)
        if vec is None:
            return []

        vocab = list(self.glove_vectors.keys())
        vectors = np.array([self.glove_vectors[w] for w in vocab])
        similarities = cosine_similarity([vec], vectors)[0]
        top_indices = similarities.argsort()[::-1][1:top_n + 1]

        return [(vocab[i], float(similarities[i])) for i in top_indices]

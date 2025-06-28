# visualizer.py

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

def reduce_dimensions(vectors, method="pca", n_components=2):
    if method == "tsne":
        model = TSNE(n_components=n_components, perplexity=5, random_state=42)
    else:
        model = PCA(n_components=n_components)
    return model.fit_transform(vectors)

def plot_words(words, vectors_2d, filename="static/plot.png"):
    plt.figure(figsize=(8, 6))
    for i, word in enumerate(words):
        x, y = vectors_2d[i]
        plt.scatter(x, y)
        plt.text(x+0.01, y+0.01, word)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

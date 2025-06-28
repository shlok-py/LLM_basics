# word_embedding_app/main.py

from flask import Flask, request, jsonify, render_template
from processor.embeddings_loader import EmbeddingHandler
from processor.visualizer import reduce_dimensions, plot_words
import os

# Initialize Flask app
app = Flask(__name__)

# Sample corpus for embeddings
corpus = [
    "Artificial intelligence is transforming the world.",
    "Natural language processing enables computers to understand text.",
    "Word embeddings represent words as vectors.",
    "Machine learning is part of artificial intelligence.",
    "Deep learning models learn from data."
]

handler = EmbeddingHandler(corpus)

@app.route("/")
def home():
    return render_template("embedding_ui.html")

@app.route("/embedding", methods=["POST"])
def get_embedding():
    data = request.get_json()
    word = data.get("word", "").lower()
    vec = handler.get_vector(word)

    if vec is None:
        return jsonify({"error": "Word not found in vocabulary."}), 404

    neighbors = handler.get_nearest_neighbors(word)
    words = [word] + [w for w, _ in neighbors]
    vectors = [handler.get_vector(w) for w in words]
    vectors_2d = reduce_dimensions(vectors, method="pca")

    # ✅ Ensure static directory exists
    if not os.path.exists("static"):
        os.makedirs("static")

    plot_path = os.path.join("static", "plot.png")
    plot_words(words, vectors_2d, filename=plot_path)

    return jsonify({
        "word": word,
        "vector": vec.tolist(),
        "neighbors": neighbors,
        "plot": "/static/plot.png"
    })


if __name__ == "__main__":
    app.run(debug=True)

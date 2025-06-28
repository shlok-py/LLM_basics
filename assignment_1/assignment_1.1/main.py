from flask import Flask, request, jsonify, render_template
from processor.spacy_processor import process_text_spacy
from processor.nltk_processor import process_text_nltk

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze_text():
    data = request.get_json()
    text = data.get("text", "")
    engine = data.get("engine", "spacy").lower()

    if not text:
        return jsonify({"error": "Text is required."}), 400

    try:
        if engine == "spacy":
            result = process_text_spacy(text)
        elif engine == "nltk":
            result = process_text_nltk(text)
        else:
            return jsonify({"error": "Invalid engine. Use 'spacy' or 'nltk'."}), 400

        # Convert tuples to lists for JSON serialization
        for key in ["pos_tags", "named_entities"]:
            if key in result:
                result[key] = [list(item) for item in result[key]]

        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

from processor.shared_utils import lemmatize_and_stem_comparison

@app.route("/compare", methods=["POST"])
def compare_lemma_stem():
    data = request.get_json()
    text = data.get("text", "")
    engine = data.get("engine", "nltk").lower()

    if not text:
        return jsonify({"error": "Text is required."}), 400

    try:
        result = lemmatize_and_stem_comparison(text, engine)
        return jsonify({"comparison": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)

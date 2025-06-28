# shared_utils.py

import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
import spacy

nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('omw-1.4', quiet=True)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
nlp_spacy = spacy.load("en_core_web_sm")

# POS mapping for nltk lemmatizer
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    return wordnet.NOUN

def lemmatize_and_stem_comparison(text: str, engine: str = "nltk"):
    results = []

    if engine.lower() == "nltk":
        tokens = word_tokenize(text)
        pos_tags = pos_tag(tokens)
        for token, tag in pos_tags:
            wn_tag = get_wordnet_pos(tag)
            lemma = lemmatizer.lemmatize(token, wn_tag)
            stem = stemmer.stem(token)
            results.append({
                "word": token,
                "stem": stem,
                "lemma": lemma
            })

    elif engine.lower() == "spacy":
        doc = nlp_spacy(text)
        for token in doc:
            results.append({
                "word": token.text,
                "stem": token.text[:4] + "..." if len(token.text) > 4 else token.text,  # spaCy doesn't support stemming directly
                "lemma": token.lemma_
            })

    else:
        raise ValueError("Invalid engine: choose 'nltk' or 'spacy'")

    return results
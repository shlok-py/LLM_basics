import spacy

nlp = spacy.load("en_core_web_sm")

def process_text_spacy(text):
    doc = nlp(text)
    return {
        "tokens": [token.text for token in doc],
        "lemmas": [token.lemma_ for token in doc],
        "pos_tags": [(token.text, token.pos_) for token in doc],
        "named_entities": [(ent.text, ent.label_) for ent in doc.ents]
    }

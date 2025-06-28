import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag, ne_chunk
from nltk.tree import Tree

# Ensure required data is downloaded
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
nltk.download('wordnet')
nltk.download('omw-1.4')

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def extract_named_entities(chunked):
    entities = []
    for chunk in chunked:
        if isinstance(chunk, Tree):
            entity = " ".join(c[0] for c in chunk)
            label = chunk.label()
            entities.append((entity, label))
    return entities

def process_text_nltk(text):
    tokens = word_tokenize(text)
    stems = [stemmer.stem(token) for token in tokens]
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    pos_tags = pos_tag(tokens)
    chunked = ne_chunk(pos_tags)
    named_entities = extract_named_entities(chunked)

    return {
        "tokens": tokens,
        "stems": stems,
        "lemmas": lemmas,
        "pos_tags": pos_tags,
        "named_entities": named_entities
    }

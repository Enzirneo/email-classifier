import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# baixa apenas 1x (chamado no startup)
def ensure_nlp_resources():
    try:
        nltk.data.find("corpora/stopwords")
    except LookupError:
        nltk.download("stopwords")
    try:
        nltk.data.find("corpora/wordnet")
    except LookupError:
        nltk.download("wordnet")

_stop_words = None
_lemmatizer = None

def _lazy_init():
    global _stop_words, _lemmatizer
    if _stop_words is None:
        # pt + en (muitas caixas terão conteúdo misto)
        langs = []
        try:
            langs.extend(stopwords.words("portuguese"))
        except Exception:
            pass
        try:
            langs.extend(stopwords.words("english"))
        except Exception:
            pass
        _stop_words = set(langs) if langs else set()
    if _lemmatizer is None:
        _lemmatizer = WordNetLemmatizer()

def preprocess(text: str) -> str:
    """
    Limpa, normaliza, remove stopwords e lematiza.
    """
    _lazy_init()
    text = (text or "").lower()
    text = re.sub(r"http\S+|www\.\S+", " ", text)         # links
    text = re.sub(r"[^a-zà-úçãõâêôíóúáé0-9\s]", " ", text) # pontuação
    tokens = text.split()
    tokens = [t for t in tokens if t not in _stop_words and len(t) > 1]
    # lematização apenas para palavras “inglesas”; para PT é ok manter
    tokens = [ _lemmatizer.lemmatize(t) for t in tokens ]
    return " ".join(tokens)

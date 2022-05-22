from sumy.utils import get_stop_words
from sumy.nlp.stemmers import Stemmer
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lex_rank import LexRankSummarizer as Summarizer

import nltk
nltk.download('punkt')

LANGUAGE = "english"

# configurable number of sentences
SENTENCES_COUNT = 5

def get_summary(text):
    # text cleaning
    text = "".join(text).replace("\n", " ").replace('"', "")

    parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    article_summary = []
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        article_summary.append(str(sentence))

    clean_summary = ' '.join([str(elem) for elem in article_summary])

    return clean_summary
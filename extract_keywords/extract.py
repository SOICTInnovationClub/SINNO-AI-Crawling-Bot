import spacy
import pytextrank
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
nltk.download('stopwords')

df = pd.read_csv('data.csv')
keywordLists = []

def return_keywords(text) :
    keywords = []
    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm")
    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")
    doc = nlp(text)
    # examine the top-ranked phrases in the document
    for phrase in doc._.phrases[:10]:
        keywords.append(phrase.text)
    return keywords

def remove_stopword(text):
    text_tokens = word_tokenize(text)
    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
    return ' '.join(tokens_without_sw)

for my_text in df['Body']:
    short_text = remove_stopword(my_text)
    keywordList = return_keywords(short_text)
    
    keywordLists.append(keywordList)
df["Keywords_Spicy2"] =keywordLists
df.to_csv("data.csv", index=False) 
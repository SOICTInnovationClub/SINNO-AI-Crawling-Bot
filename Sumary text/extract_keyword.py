from rake_nltk import Rake
import nltk
from nltk import tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
nltk.download('stopwords')
nltk.download('punkt')

df = pd.read_csv('data.csv')
r = Rake()
keywordLists = []

def remove_stopword(text):
    text_tokens = word_tokenize(text)
    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
    return ' '.join(tokens_without_sw)

for my_text in df['Body']:
    short_text = remove_stopword(my_text)
    r.extract_keywords_from_text(short_text)
    keywordList           = []
    rankedList            = r.get_ranked_phrases_with_scores()
    for keyword in rankedList:
        keyword_updated       = keyword[1].split()
        keyword_updated_string    = " ".join(keyword_updated[:2])
        keywordList.append(keyword_updated_string)
        if(len(keywordList)>9):
            break
    keywordLists.append(keywordList)
df["Keywords"] =keywordLists
df.to_csv("data.csv", index=False) 
from rake_nltk import Rake
import nltk
import pandas as pd
nltk.download('stopwords')
nltk.download('punkt')

df = pd.read_csv('iotnews.csv')
r = Rake()
keywordLists = []
for my_text in df['Body']:


    r.extract_keywords_from_text(my_text)
    keywordList           = []
    rankedList            = r.get_ranked_phrases_with_scores()
    for keyword in rankedList:
        keyword_updated       = keyword[1].split()
        keyword_updated_string    = " ".join(keyword_updated[:2])
        keywordList.append(keyword_updated_string)
        if(len(keywordList)>9):
            break
    keywordLists.append(keywordList)
df["keywords"] =keywordLists
df.to_csv("iotnews.csv", index=False) 

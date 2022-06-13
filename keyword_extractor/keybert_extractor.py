from keybert import KeyBERT
import pandas as pd
csv_list = ['../data/arstechnica_data.csv','../data/techcrunch_data.csv','../data/theverge_data.csv']
kw_model = KeyBERT()
for csv in csv_list:
    data = pd.read_csv(csv)
    keywords=[]
    for doc in data['Body']:
        keywordsList = [item[0] for item in kw_model.extract_keywords(doc, keyphrase_ngram_range=(1, 2), stop_words='english', 
                                                                    use_mmr=True, diversity=0.5)]
        keywords.append(keywordsList)
    data['keywords']=keywords
    data.to_csv(csv, encoding='utf-8-sig', index=False)
        
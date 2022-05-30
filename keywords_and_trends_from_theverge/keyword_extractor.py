from rake_nltk import Rake
import pandas as pd
import seaborn as sns

r = Rake()
file = pd.read_csv('data.csv')
keywordList = {}
for my_text in file.loc[:,'Body']:
  r.extract_keywords_from_text(my_text)
  rankedList = r.get_ranked_phrases_with_scores()[:10]
  for keyword in rankedList:
    keyword_updated = keyword[1].split()
    keyword_updated_string = " ".join(keyword_updated[:3])
    print(keyword_updated_string)
    if(not (keyword_updated_string in list(keywordList.keys()))):
      keywordList[keyword_updated_string]=0
    keywordList[keyword_updated_string]+=1
  print('\n')
keywordList={k: v for k, v in sorted(keywordList.items(), key=lambda item: item[1])}
kw_data = pd.DataFrame({'trends':list(keywordList.keys())[:10],
                    'popularity':list(keywordList.values())[:10]})
plot_data=kw_data.head(5)
kw_plot=sns.barplot(x="trends",y="popularity",data=plot_data)
kw_plot.figure.savefig("trends.png")
kw_data.to_csv("kw_data.csv", encoding='utf-8-sig', index=False)
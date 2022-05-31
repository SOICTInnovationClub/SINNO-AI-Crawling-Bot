from bs4 import BeautifulSoup
# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lex_rank import LexRankSummarizer
# from sumy.summarizers.luhn import LuhnSummarizer
# from sumy.summarizers.lsa import LsaSummarizer
# from rouge import Rouge 
import requests
import pandas as pd

ARTICLES_COUNT = 15
titles_data = []
links_data = []
paragraphs = []
Sumy_lex_rank = []
Sumy_luhn = []
Sumy_lsa = []
references = []
f1_lex_rank = []
f1_luhn = []
f1_lsa = []

# def final(result,r):
#     if r!="":
#         scores = rouge.get_scores(result, r)
#         return scores[0]["rouge-1"]["f"]       
    
# def lex_rank(p):
#     summarizer = LexRankSummarizer()
#     summary = summarizer(parser.document,2) #summarize into 2 sentences
#     return str(summary[0])+' '+str(summary[1])

# def luhn(p):
#     summarizer = LuhnSummarizer()
#     summary = summarizer(parser.document,2)
#     return str(summary[0])+' '+str(summary[1])

# def lsa(p):
#     summarizer = LsaSummarizer()
#     summary = summarizer(parser.document,2)
#     return str(summary[0])+' '+str(summary[1])

def body(url) :   
    article = requests.get(url)
    doc = BeautifulSoup(article.text, "html.parser")
    if(doc.find('div', attrs={'class':'article-content'}) is None):
        titles_data.pop()
        links_data.pop()
    else: 
        bodies = doc.find('div', attrs={'class':'article-content'}).find_all('p')
        for paragraph in bodies:
            for match in paragraph.find_all('a'):
                match.replaceWithChildren()
        bodies = [paragraph.text for paragraph in bodies]
        body = ' '.join(bodies)
        paragraphs.append(body)

        
def article_links_and_title(url) :
    page = requests.get(url)
    doc = BeautifulSoup(page.text, "html.parser")
    titles_and_links = [header.a for header in doc.find_all('h2', attrs={'class':'post-block__title'})[:ARTICLES_COUNT]] 
    for row in titles_and_links:
        link = row.attrs['href']
        title = row.text.strip()
        titles_data.append(title)
        links_data.append(link)    

url = "https://techcrunch.com/"
article_links_and_title(url)
for link in links_data:
    body(link)
# rouge = Rouge()
# for p in paragraphs:
#     if len(p)<300: # too short to summarize in 2 sentences
#         Sumy_lex_rank.append("")
#         Sumy_luhn.append("")
#         Sumy_lsa.append("")
#         references.append("")
#         f1_lex_rank.append("")
#         f1_luhn.append("")
#         f1_lsa.append("")
#         continue
#     print(p+'\n')
#     reference = input("Your summary:")
#     print('\n')
#     references.append(reference)
#     parser = PlaintextParser.from_string(p,Tokenizer("english"))
#     result = lex_rank(parser)
#     f1_lex_rank.append(final(result,reference))
#     Sumy_lex_rank.append(result)
#     result = luhn(parser)
#     f1_luhn.append(final(result,reference))
#     Sumy_luhn.append(result)
#     result = lsa(parser)
#     f1_lsa.append(final(result,reference))
#     Sumy_lsa.append(result)

data = pd.DataFrame({'Title': titles_data,
                    'Link': links_data,
                    'Body': paragraphs})
data.to_csv("../data/techcrunch_data.csv", encoding='utf-8-sig', index=False)
# df = pd.DataFrame({'Title': titles_data,
#                    'Link': links_data,
#                   'Original paragraphs': paragraphs,
#                   'reference summary': references,
#                   'r1 f1 score lex rank': f1_lex_rank,
#                   'Sumy summary using lex rank': Sumy_lex_rank,
#                   'r1 f1 score luhn': f1_luhn,
#                   'Sumy summary using Luhn': Sumy_luhn,
#                   'r1 f1 score lsa': f1_lsa,
#                   'Sumy summary using LSA': Sumy_lsa})
# df.to_csv("summarization.csv", encoding='utf-8-sig', index=False) 











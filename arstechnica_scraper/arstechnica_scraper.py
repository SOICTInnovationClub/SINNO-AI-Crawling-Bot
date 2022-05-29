from bs4 import BeautifulSoup
import requests
import pandas as pd

ARTICLES_COUNT = 10
titles_data = []
links_data = []
paragraphs = []

def body(url) :   
    article = requests.get(url)
    doc = BeautifulSoup(article.text, "html.parser")
    
    bodies = doc.find_all('p')[4:6] 
    bodies = [paragraph.text.strip() for paragraph in bodies]
    body = ' '.join(bodies)
    paragraphs.append(body)
        
def article_links_and_title(url) :
    page = requests.get(url)
    doc = BeautifulSoup(page.text, "html.parser")
    
    titles_and_links = [header.a for header in doc.find_all('h2')[:ARTICLES_COUNT]] 
    for row in titles_and_links:
        link = row.attrs['href']
        title = row.text.strip()
        titles_data.append(title)
        links_data.append(link)  

url = "https://arstechnica.com/"
article_links_and_title(url)
for link in links_data:
    body(link)

df = pd.DataFrame({'Title': titles_data,
                   'Link': links_data,
                  'Body': paragraphs})
df.to_csv("data.csv", encoding='utf-8-sig', index=False)
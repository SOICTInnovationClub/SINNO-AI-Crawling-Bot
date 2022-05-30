from bs4 import BeautifulSoup
import requests
import pandas as pd

ARTICLES_COUNT = 15
titles_data = []
links_data = []
paragraphs = []

def body(url) :   
    article = requests.get(url)
    doc = BeautifulSoup(article.text, "html.parser")
    
    bodies = doc.find('div', attrs={'class':'c-entry-content'}).find_all('p')[0:4] 
    for paragraph in bodies:
        for match in paragraph.find_all('a'):
            for emphasized in match.find_all('em'):
                emphasized.replaceWithChildren()
            match.replaceWithChildren()    
    bodies = [paragraph.text.strip() for paragraph in bodies]
    body = ' '.join(bodies)
    paragraphs.append(body)
        
def article_links_and_title(url) :
    page = requests.get(url)
    doc = BeautifulSoup(page.text, "html.parser")
    
    titles_and_links = [header.a for header in doc.find_all('h2', attrs={'class':'c-entry-box--compact__title'})[:ARTICLES_COUNT]] 
    for row in titles_and_links:
        link = row.attrs['href']
        title = row.text.strip()
        titles_data.append(title)
        links_data.append(link)  

url = "https://www.theverge.com/tech"
article_links_and_title(url)
for link in links_data:
    body(link)

df = pd.DataFrame({'Title': titles_data,
                   'Link': links_data,
                  'Body': paragraphs})
df.to_csv("data.csv", encoding='utf-8-sig', index=False)
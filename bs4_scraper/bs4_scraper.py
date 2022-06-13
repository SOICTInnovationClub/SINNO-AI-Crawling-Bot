from bs4 import BeautifulSoup
import requests
url = "https://www.nature.com/articles/d41586-022-01320-y"
page = requests.get(url)
doc = BeautifulSoup(page.text, "html.parser")
links = doc.find('article').find_all('a')
f = open('./data/links.txt','a')
f.write(str(doc.find('h1').string)+'\n')
for link in links:
    if ('href' in link.attrs) and ('http' in str(link.attrs['href'])):
        f.write(str(link.attrs['href'])+'\n')
f.close()

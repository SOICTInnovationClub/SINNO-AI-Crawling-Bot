from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import pandas as pd
import random
from selenium.webdriver.common.by import By

PAGE_NUMBER = 20
titles_data = []
bodies_data = []
links_data = []
page_list = ['https://www.iottechnews.com/']

def crawl_body(url) :
    '''Input: string url is the link to the article that we need to crawl its body
       Output: return its body in a dictionary which keys are also title and body'''
    
    browser = webdriver.Chrome(executable_path=r"C:\Users\THU HIEN\chromedriver\chromedriver.exe")
    browser.get(url)
    sleep(random.uniform(2, 3)) 
    
    bodies = browser.find_elements(By.TAG_NAME, "p")
    bodies = [body.text for body in bodies[:-10]]
    
    body = ' '.join(bodies)
    
    
    return body
        
def return_article_links_and_title(url) :
    '''Input: string url is the link of page that we need to crawl. This page must be from nature.com
    Output: Return a list that include all the article's link from this page'''
    browser = webdriver.Chrome(executable_path=r"C:\Users\THU HIEN\chromedriver\chromedriver.exe")   
    browser.get(url)
    sleep(random.uniform(4, 8))    #sleep to load all the title, random num to be not recognized as a bot

    titles_and_links = browser.find_elements(By.CLASS_NAME, 'img-link')
    
    titles_data = []
    links_data = []
    for row in titles_and_links:
        link = row.get_attribute('href') # link to this article
        title = row.get_attribute('title')

        titles_data.append(title)
        links_data.append(link)
        print(link)
    return {'titles': titles_data, 'links': links_data}        

for page in page_list :
    links = return_article_links_and_title(page)['links']
    titles = return_article_links_and_title(page)['titles']
    for link in links :
        body = crawl_body(link)
        bodies_data.append(body)
        links_data.append(link)
    for title in titles :
        titles_data.append(title)

df = pd.DataFrame({'Title': titles_data,
                   'Link': links_data,
                  'Body': bodies_data})
# Export data to csv file, contain two columns that is title column and link column
df.to_csv("iotnews.csv", index=False)      
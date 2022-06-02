from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import pandas as pd
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# From NgocQuan with LOVE 
def the_time_now() :
    import datetime
    now = datetime.datetime.now()
    time = now.strftime("%Y%m%d%H%M%S")
    return time
    
PAGE_NUMBER = 20
titles = []
bodies = []
links = []
def return_article_links(url) :
    '''Input: string url is the link of page that we need to crawl. This page must be from nature.com
    Output: Return a list that include all the article's link from this page'''
    article_links = []
    browser = webdriver.Chrome(executable_path="./chromedriver.exe")
    browser.get(url)
    sleep(random.uniform(2, 3)) 

    cookie = browser.find_element(By.XPATH, "/html/body/section/div/div[2]/button[1]")
    cookie.click()
    sleep(random.uniform(4, 6)) 
    tag_names_a = browser.find_elements(By.TAG_NAME, 'a')

    for row in tag_names_a :
        link = row.get_attribute('href')
        article_link_format = 'https://www.nature.com/articles/'
        if article_link_format in link :
            article_links.append(link)
    browser.close()
    return article_links

def crawl_body_and_title(url) :
    '''Input: string url is the link to the article that we need to crawl its title and body
       Output: return its title and its body in a dictionary which keys are also title and body'''
    
    browser = webdriver.Chrome(executable_path="./chromedriver.exe")
    browser.get(url)
    
    sleep(random.uniform(2, 3)) 
    title = browser.find_element(By.XPATH, '/html/body/div[2]/div/article/div/main/div[1]/header/div[1]/h1')
    body = browser.find_element(By.XPATH, "/html/body/div[2]/div/article/div/main/div[1]/header/div[1]/div/div")

    title = title.text
    body = body.text
    return {'title': title, 'body': body, 'url': url}

page_list = []
page_1 = 'https://www.nature.com/research-analysis'
page_list.append(page_1)
if PAGE_NUMBER > 1 :
    for i in range(2, PAGE_NUMBER+1) :
        page_list.append(f'https://www.nature.com/research-analysis?page={i}')
    
for page in page_list :
    article_links = return_article_links(page)
    for url in article_links :
        title_and_body = crawl_body_and_title(url)
        title = title_and_body['title']
        body = title_and_body['body']
        link = title_and_body['url']
        titles.append(title)
        bodies.append(body)
        links.append(link)
        
df = pd.DataFrame({'Article Link': link,
                   'Title': titles,
                   'Body': bodies})
# Export data to csv file, contain two columns that is title column and link column
time = the_time_now()
df.to_csv("nature.csv", index=False)    

        
    


                
    
            
            
    
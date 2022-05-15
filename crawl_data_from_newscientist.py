from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import pandas as pd
import random
from selenium.webdriver.common.by import By

# From NgocQuan with LOVE 

browser = webdriver.Chrome(executable_path="./chromedriver.exe")

titles_data = []
links_data = []
PAGES = 5 # The number of pages that we must crawl

for i in range(2, PAGES + 2) :
    

    url = 'https://www.newscientist.com/subject/technology/page/{}/'.format(str(i))
    print(11111111111, i)
    browser.get(url)
    sleep(random.uniform(4, 9))    #sleep to load all the title, random num to be not recognized as a bot

    titles = browser.find_elements(By.CLASS_NAME, 'card__link')
    for row in titles:
        link = row.get_attribute('href') # link to this article
    
        title = link[link.find('-'):] 
        title = title.replace('-', ' ')
        title = title.replace('/', '')
        title = title.capitalize()
    
        titles_data.append(title)
        links_data.append(link)
        
        


df = pd.DataFrame({'Title': titles_data,
                   'Link': links_data})
# Export data to csv file, contain two columns that is title column and link column
df.to_csv("newscientist.csv", index=False)    
browser.close()
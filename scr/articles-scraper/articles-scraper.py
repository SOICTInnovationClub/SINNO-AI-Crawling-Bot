from newspaper import Article, Config
import pandas as pd

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'

config = Config()
config.browser_user_agent = USER_AGENT
config.request_timeout = 10

filename = '20-5-2022-9'

newspapers = pd.read_csv(f'./data/{filename}.csv')

url = newspapers['URL'][10]
print(url)

article = Article(url, config=config)
article.download()
article.parse()

print(article.authors)
print(article.text)

article_meta_data = article.meta_data
article_summary = {value for (key, value) in article_meta_data.items() if key == 'article.summary'}
print(article_summary)

keywords = ''.join({value for (key, value) in article_meta_data.items() if key == 'news_keywords'})
article_keywords = sorted(keywords.lower().split(','))
print(article_keywords)
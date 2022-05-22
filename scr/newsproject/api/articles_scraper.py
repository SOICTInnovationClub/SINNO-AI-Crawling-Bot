from newspaper import Article, Config

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'

config = Config()
config.browser_user_agent = USER_AGENT
config.request_timeout = 10

def get_article(url):
    article = Article(url, config=config)
    article.download()
    article.parse()

    res = {
        'title': article.title, 
        'text': article.text,
        'image': article.top_image,
    }

    return res
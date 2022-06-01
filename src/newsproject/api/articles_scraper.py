from newspaper import Article, Config

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'

config = Config()
config.browser_user_agent = USER_AGENT
config.request_timeout = 20

def get_article(url):
    try:
        article = Article(url, config=config)
        article.download()
        article.parse()
    except Exception as e:
        print(e)

    source = url.split('/')[2]

    res = {
        'title': article.title, 
        'text': article.text,
        'image': article.top_image,
        'pub_date': article.publish_date,
        'publisher': source,
    }

    if len(article.text.split()) < 100:
        res['text'] = article.meta_description

    return res
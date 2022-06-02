from datetime import datetime
from django.utils.timezone import make_aware
from newsapp.models import NewsArticle
from api.reddit_scraper import get_subreddit_posts
from api.articles_scraper import get_article
from api.summary import get_summary
from api.csv_scraper import get_csv_articles

def fetch_news_articles(): 
    NewsArticle.objects.all().delete()

    print("Getting articles from reddit")

    articles = get_subreddit_posts()

    for article in articles:
        url = article['url']
        if not NewsArticle.objects.filter(url=url).exists():
            res = get_article(url)
            title = res['title'] or article['title']
            text = res['text']
            top_image = res['image']
            pub_date = None
            publisher = res['publisher']

            if res['text']:
                summary = get_summary(text)

                print(url)

                NewsArticle.objects.create(
                    title=title,
                    url=url,
                    body=text,
                    top_image=top_image,
                    summary=summary,
                    publisher=publisher,
                    pub_date=pub_date,
                    source='reddit'
                )

    print("Getting articles from csv")
        
    urls = get_csv_articles()
    for url in urls:
        if not NewsArticle.objects.filter(url=url).exists():
            res = get_article(url)
            title = res['title']
            text = res['text']
            top_image = res['image']
            try:
                if res['pub_date']:
                    pub_date = make_aware(res['pub_date'])
                else:
                    pub_date = None
            except ValueError:
                pub_date = res['pub_date']
            publisher = res['publisher']

            if res['text']:
                summary = get_summary(text)

                print(url)

                NewsArticle.objects.create(
                    title=title,
                    url=url,
                    body=text,
                    top_image=top_image,
                    summary=summary,
                    publisher=publisher,
                    pub_date=pub_date,
                    source='csv'
                )

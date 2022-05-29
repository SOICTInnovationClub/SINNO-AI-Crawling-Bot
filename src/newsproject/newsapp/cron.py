from newsapp.models import NewsArticle
from api.reddit_scraper import get_subreddit_posts
from api.articles_scraper import get_article
from api.summary import get_summary

def fetch_news_articles(): 
    NewsArticle.objects.all().delete()

    articles = get_subreddit_posts()

    for article in articles:
        url = article['url']
        if not NewsArticle.objects.filter(url=url).exists():
            res = get_article(url)
            title = res['title'] or article['title']
            text = res['text']
            top_image = res['image']
            pub_date = res['pub_date']
            publisher = res['publisher']

            summary = get_summary(text)

            NewsArticle.objects.create(
                title=title,
                url=url,
                body=text,
                top_image=top_image,
                summary=summary,
                publisher=publisher,
            )
        
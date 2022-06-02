import praw
from api import ignored_sources

def get_subreddit_posts(thread='technology', limit_nposts=20):
    reddit = praw.Reddit(
        client_id='pVnJ9rA-oFsfsdgPAwOH2w',
        client_secret='Am0JSg1Py9J0S2FydJIkioDdq4wqYA',
        user_agent='tech-links-scraper',
        username='Adventurous-Bed-8571',
        password='123456789!',
    )

    subreddit = reddit.subreddit(thread)

    hot_news = subreddit.hot()

    articles = []

    nposts = 0

    for submission in hot_news:
        source = submission.url.split('/')[2]

        if (not submission.stickied) and (source not in ignored_sources) and (nposts < limit_nposts):          
            nposts += 1
            article = {}
            article['title'] = submission.title
            article['url'] = submission.url
            articles.append(article)

    return articles
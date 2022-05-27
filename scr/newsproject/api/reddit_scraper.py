import praw
from api.articles_scraper import get_article
from api.summary import get_summary

def get_subreddit_posts(thread='technology', num_posts=20):
    reddit = praw.Reddit(
        client_id='pVnJ9rA-oFsfsdgPAwOH2w',
        client_secret='Am0JSg1Py9J0S2FydJIkioDdq4wqYA',
        user_agent='tech-links-scraper',
        username='Adventurous-Bed-8571',
        password='123456789!',
    )

    subreddit = reddit.subreddit(thread)

    hot_news = subreddit.hot(limit=num_posts)

    data = {'titles': [], 'urls': [], 'summary': [], 'images': []}

    for submission in hot_news:
        if not submission.stickied:
            data['titles'].append(submission.title)
            data['urls'].append(submission.url)

            article = get_article(submission.url)
            summary = get_summary(article['text'])
            data['summary'].append(summary)

            data['images'].append(article['image'])

    return data
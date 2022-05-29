import praw

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

    articles = []

    for submission in hot_news:
        if not submission.stickied:
            article = {}
            article['title'] = submission.title
            article['url'] = submission.url
            articles.append(article)

    return articles
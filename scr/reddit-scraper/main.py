import praw
import datetime

reddit = praw.Reddit()

subreddit = reddit.subreddit('technology')

hot_news = subreddit.hot(limit=20)

date = datetime.datetime.now()

filename = f'{date.day}-{date.month}-{date.year}-{date.hour}.txt'

with open(f'./data/{filename}', 'w') as f:
    for submission in hot_news:
        if not submission.stickied:
            f.write(f'{submission.title}\n')
            f.write(f'{submission.url}\n')




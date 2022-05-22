import praw
import datetime
import pandas as pd

reddit = praw.Reddit()

subreddit = reddit.subreddit('technology')

hot_news = subreddit.hot(limit=20)

date = datetime.datetime.now()

filename = f'{date.day}-{date.month}-{date.year}-{date.hour}'

titles = []
urls = []

for submission in hot_news:
    if not submission.stickied:
        titles.append(submission.title)
        urls.append(submission.url)

df = pd.DataFrame({'Title': titles, 'URL': urls})
df.to_csv(f'../data/{filename}.csv', index=False)
import praw

reddit = praw.Reddit()

subreddit = reddit.subreddit('technology')

hot_news = subreddit.hot(limit=10)

for submission in hot_news:
    if not submission.stickied:
        print(submission.title)
        print(submission.url)
        print('\n')
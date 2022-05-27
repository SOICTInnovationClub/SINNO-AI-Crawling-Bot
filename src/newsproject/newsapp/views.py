from turtle import title
from django.shortcuts import render
from api.reddit_scraper import get_subreddit_posts

# Create your views here.
def index(request):
    posts = get_subreddit_posts(thread='technology', num_posts=20)

    title = posts['titles']
    url = posts['urls']
    summary = posts['summary']
    image = posts['images']

    news = zip(title, url, image, summary)
    
    return render(request, 'newsapp/index.html', {'news': news})
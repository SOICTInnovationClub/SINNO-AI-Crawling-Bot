from django.shortcuts import render
from .models import NewsArticle

def index(request):
    context = {
        'reddit_news': NewsArticle.objects.filter(source='reddit')[:3],
        'theverge_news': NewsArticle.objects.filter(publisher='www.theverge.com', source='csv')[:3],
        'techcrunch_news': NewsArticle.objects.filter(publisher='techcrunch.com', source='csv')[:3],
        'iot_news': NewsArticle.objects.filter(publisher='www.iottechnews.com', source='csv')[:3],
        'ai_news': NewsArticle.objects.filter(publisher='www.artificialintelligence-news.com', source='csv')[:3],
        'arstechnica_news': NewsArticle.objects.filter(publisher='arstechnica.com', source='csv')[:3],
    }
    
    return render(request, 'newsapp/index.html', context)
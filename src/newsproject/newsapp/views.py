from django.shortcuts import render
from matplotlib.style import context
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

def reddit(request):
    context = {
        'news_set': NewsArticle.objects.filter(source='reddit'),
    }
    return render(request, 'newsapp/more.html', context)

def theverge(request):
    context = {
        'news_set': NewsArticle.objects.filter(publisher='www.theverge.com', source='csv').order_by('-pub_date'),
    }
    return render(request, 'newsapp/more.html', context)

def techcrunch(request):
    context = {
        'news_set': NewsArticle.objects.filter(publisher='techcrunch.com', source='csv').order_by('-pub_date'),
    }
    return render(request, 'newsapp/more.html', context)

def iotnews(request):
    context = {
        'news_set': NewsArticle.objects.filter(publisher='www.iottechnews.com', source='csv').order_by('-pub_date'),
    }
    return render(request, 'newsapp/more.html', context)

def ainews(request):
    context = {
        'news_set': NewsArticle.objects.filter(publisher='www.artificialintelligence-news.com', source='csv').order_by('-pub_date'),
    }
    return render(request, 'newsapp/more.html', context)

def arstechnica(request):
    context = {
        'news_set': NewsArticle.objects.filter(publisher='arstechnica.com', source='csv'),
    }
    return render(request, 'newsapp/more.html', context)
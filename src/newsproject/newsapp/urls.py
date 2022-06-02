from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('reddit', views.reddit),
    path('theverge', views.theverge),
    path('techcrunch', views.techcrunch),
    path('iotnews', views.iotnews),
    path('ainews', views.ainews),
    path('arstechnica', views.arstechnica),
]
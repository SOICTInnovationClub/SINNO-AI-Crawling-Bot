from django.db import models
import json
class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    body = models.TextField(null=True, blank=True)
    top_image = models.URLField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    publisher = models.CharField(max_length=100, null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    keywords = models.CharField(max_length=200, null=True, blank=True)

    def get_keywords(self):
        return self.keywords.split('|')
        
    def __str__(self):
        return self.title
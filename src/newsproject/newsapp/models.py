from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200, primary_key=True)
    body = models.TextField(null=True, blank=True)
    top_image = models.URLField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    publisher = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title
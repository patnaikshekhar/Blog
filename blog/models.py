from django.db import models
from django.utils import timezone
# Create your models here.
"""
The main article class, used to create the actual blog entries
"""
class Article(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    date = models.DateTimeField()
    likes = models.IntegerField(default=0)

"""
The comments class used to add comments to the blog
"""
class Comments(models.Model):
    article = models.ForeignKey(Article)
    name = models.CharField(max_length=200)
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now())

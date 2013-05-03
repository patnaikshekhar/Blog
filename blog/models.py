from django.db import models
from django.utils import timezone


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


"""
This is the class which holds the data about the open
source projects which i'm working on
"""
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=50, default='In Progress')
    start_date = models.DateTimeField(default=timezone.now())
    git_hub_link = models.TextField()

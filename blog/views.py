from django.shortcuts import render

from blog.models import Article, Comments

"""
The homepage view is rendered here
"""
def index(request):
    latest_articles = Article.objects.all().order_by('-date')[:3]
    context = {'latest_articles': latest_articles}
    return render(request, 'blog/index.html', context)

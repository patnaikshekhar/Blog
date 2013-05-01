from django.shortcuts import render, get_object_or_404

from blog.models import Article, Comments


"""
The homepage view is rendered here
"""
def index(request):
    latest_articles = Article.objects.all().order_by('-date')[:3]
    context = {'latest_articles': latest_articles}
    return render(request, 'blog/index.html', context)


"""
This view handles displays the details of the blog,
including the comments
"""
def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/details.html', {'article': article})


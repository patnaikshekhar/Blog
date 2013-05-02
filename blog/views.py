from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone

from blog.models import Article, Comments
from blog.helperclasses import Archive

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
    comments = article.comments_set.all().order_by('-date')
    return render(request, 'blog/details.html', {'article': article, 'comments': comments})


"""
This view handles the addition of a comment. Once a
comment has been added to the database it redirects
back to the blog details page
"""
def addComment(request, article_id):
    if request.POST['comment'] != "":
        article = get_object_or_404(Article, pk=article_id)
        comment = Comments()
        comment.article = article
        if request.POST['name'] != "":
            comment.name = request.POST['name']
        else:
            comment.name = 'Unknown'
        comment.comment = request.POST['comment']
        comment.date = timezone.now()
        comment.save()

    return HttpResponseRedirect(reverse('detail', args=(article.id,)))


"""
This view has been created to handle the archive page.
The input to the view is created by looking for a valid
year month combination and sending along the article ids
"""
def archive(request):
    archive = Archive()
    for article in Article.objects.all():
        archive.add(article)
    archive.sort()
    return render(request, 'blog/archive.html' , {'archive': archive})

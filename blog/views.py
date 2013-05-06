from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone

from blog.models import Article, Comments, Project
from blog.helperclasses import Archive


"""
This function detects if the browser is a mobile
browser
"""
def isMobile(request):
    mobile_ua_hints = [ 'SymbianOS', 'Opera Mini', 'iPhone' ]
    mobile_uas = [
        'w3c ','acs-','alav','alca','amoi','audi','avan','benq','bird','blac',
        'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
        'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
        'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
        'newt','noki','oper','palm','pana','pant','phil','play','port','prox',
        'qwap','sage','sams','sany','sch-','sec-','send','seri','sgh-','shar',
        'sie-','siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-',
        'tosh','tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp',
        'wapr','webc','winw','winw','xda','xda-'
    ]

    mobile_browser = False
    ua = request.META['HTTP_USER_AGENT'].lower()[0:4]
    if (ua in mobile_uas):
        mobile_browser = True
    else:
        for hint in mobile_ua_hints:
            if request.META['HTTP_USER_AGENT'].find(hint) > 0:
                mobile_browser = True

    return mobile_browser


"""
The homepage view is rendered here
"""
def index(request):
    latest_articles = Article.objects.all().order_by('-date')[:3]
    context = {'latest_articles': latest_articles}
    if isMobile(request):
        return render(request, 'blog/index_m.html', context)
    else:
        return render(request, 'blog/index.html', context)


"""
This view handles displays the details of the blog,
including the comments
"""
def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = article.comments_set.all().order_by('-date')
    if isMobile(request):
        return render(request, 'blog/details_m.html', {'article': article, 'comments': comments})
    else:
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
    if isMobile(request):
        return render(request, 'blog/archive_m.html' , {'archive': archive})
    else:
        return render(request, 'blog/archive.html' , {'archive': archive})


"""
    The projects view is rendered using this function
"""
def projects(request):
    if isMobile(request):
        return render(request, 'blog/projects_m.html', {'projects': Project.objects.all()})
    else:
        return render(request, 'blog/projects.html', {'projects': Project.objects.all()})


"""
    This view renders a dummy about page
"""
def about(request):
    if isMobile(request):
        return render(request, 'blog/about_m.html')
    else:
        return render(request, 'blog/about.html')

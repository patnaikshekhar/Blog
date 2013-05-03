from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^home/', views.index, name='index'),
        url(r'^(?P<article_id>\d+)/$', views.detail, name='detail'),
        url(r'^(?P<article_id>\d+)/addComment/$', views.addComment, name='add_comment'),
        url(r'^archive/', views.archive, name='archive'),
        url(r'^projects/', views.projects, name='projects'),
        url(r'^about/', views.about, name='about'),
)

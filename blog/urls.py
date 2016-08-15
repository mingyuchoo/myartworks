from django.conf.urls import url, include

from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^(?P<section>\w+)$', views.index, name='index'),
    url(r'^(?P<section>\w+)/post/list/$', views.PostList.as_view(), name='post.list'),
    url(r'^(?P<section>\w+)/post/create/$', views.PostCreate.as_view(), name='post.create'),
    url(r'^(?P<section>\w+)/post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post.detail'),
    url(r'^(?P<section>\w+)/post/(?P<pk>[0-9]+)/update/$', views.PostUpdate.as_view(), name='post.update'),
    url(r'^(?P<section>\w+)/post/(?P<pk>[0-9]+)/delete/$', views.PostDelete.as_view(), name='post.delete'),
    url(r'^(?P<section>\w+)/post/(?P<pk>[0-9]+)/comment/create/$', views.CommentCreate.as_view(), name='comment.create'),
    url(r'^(?P<section>\w+)/post/(?P<post_pk>[0-9]+)/comment/(?P<pk>[0-9]+)/delete/$', views.CommentDelete.as_view(), name='comment.delete'),
]

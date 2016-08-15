from django.conf.urls import url, include

from . import views

app_name = 'job'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^work/tile/$', views.WorkTile.as_view(), name='work.tile'),
    url(r'^work/user/$', views.WorkUser.as_view(), name='work.user'),
    url(r'^work/create/$', views.WorkCreate.as_view(), name='work.create'),
    url(r'^work/(?P<pk>[0-9]+)/$', views.WorkDetail.as_view(), name='work.detail'),
    url(r'^work/(?P<pk>[0-9]+)/update/$', views.WorkUpdate.as_view(), name='work.update'),
    url(r'^work/(?P<pk>[0-9]+)/delete/$', views.WorkDelete.as_view(), name='work.delete'),
    url(r'^portfolio/(?P<pk>[0-9]+)/friend/$', views.work_toggle_friend, name='work.friend'),
    url(r'^portfolio/(?P<pk>[0-9]+)/bookmark/$', views.work_toggle_bookmark, name='work.bookmark'),
    url(r'^portfolio/(?P<pk>[0-9]+)/apply/$', views.work_toggle_apply, name='work.apply'),
    url(r'^portfolio/(?P<pk>[0-9]+)/share/$', views.work_toggle_share, name='work.share'),
    url(r'^work/(?P<pk>[0-9]+)/comment/create/$', views.CommentCreate.as_view(), name='comment.create'),
    url(r'^work/(?P<work_pk>[0-9]+)/comment/(?P<pk>[0-9]+)/delete/$', views.CommentDelete.as_view(), name='comment.delete'),
]

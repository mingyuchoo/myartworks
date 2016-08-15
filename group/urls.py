from django.conf.urls import url, include

from . import views

app_name = 'group'

urlpatterns = [
    url(r'^project/tile/$', views.ProjectTile.as_view(), name='project.tile'),
    url(r'^project/user/$', views.ProjectUser.as_view(), name='project.user'),
    url(r'^project/create/$', views.ProjectCreate.as_view(), name='project.create'),
    url(r'^project/(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view(), name='project.detail'),
    url(r'^project/(?P<pk>[0-9]+)/update/$', views.ProjectUpdate.as_view(), name='project.update'),
    url(r'^project/(?P<pk>[0-9]+)/delete/$', views.ProjectDelete.as_view(), name='project.delete'),
    url(r'^project/(?P<pk>[0-9]+)/bookmark/$', views.project_toggle_bookmark, name='project.bookmark'),
    url(r'^project/(?P<pk>[0-9]+)/apply/$', views.project_toggle_apply, name='project.apply'),
    url(r'^project/(?P<pk>[0-9]+)/share/$', views.project_toggle_share, name='project.share'),
    # url(r'^project/(?P<pk>[0-9]+)/membership/list/$', views.MembershipList.as_view(), name='membership.list'),
    # url(r'^project/(?P<project_pk>[0-9]+)/membership/(?P<pk>[0-9]+)/$', views.MembershipDetail.as_view(), name='membership.detail'),
    url(r'^project/(?P<project_pk>[0-9]+)/membership/(?P<pk>[0-9]+)/update/$', views.MembershipUpdate.as_view(), name='membership.update'),
    # url(r'^project/(?P<project_pk>[0-9]+)/membership/(?P<pk>[0-9]+)/delete/$', views.MembershipDelete.as_view(), name='membership.delete'),
    url(r'^project/(?P<pk>[0-9]+)/comment/create/$', views.CommentCreate.as_view(), name='comment.create'),
    url(r'^project/(?P<project_pk>[0-9]+)/comment/(?P<pk>[0-9]+)/delete/$', views.CommentDelete.as_view(), name='comment.delete'),
]

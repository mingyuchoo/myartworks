from django.conf.urls import url, include

from . import views


app_name = 'organization'

urlpatterns = [
    url(r'^team/tile/$', views.TeamTile.as_view(), name='team.tile'),
    url(r'^team/user/$', views.TeamUser.as_view(), name='team.user'),
    url(r'^team/create/$', views.TeamCreate.as_view(), name='team.create'),
    url(r'^team/(?P<pk>[0-9]+)/$', views.TeamDetail.as_view(), name='team.detail'),
    url(r'^team/(?P<pk>[0-9]+)/update/$', views.TeamUpdate.as_view(), name='team.update'),
    url(r'^team/(?P<pk>[0-9]+)/delete/$', views.TeamDelete.as_view(), name='team.delete'),
    url(r'^team/(?P<pk>[0-9]+)/bookmark/$', views.team_toggle_bookmark, name='team.bookmark'),
    url(r'^team/(?P<pk>[0-9]+)/apply/$', views.team_toggle_apply, name='team.apply'),
    url(r'^team/(?P<pk>[0-9]+)/share/$', views.team_toggle_share, name='team.share'),
    # url(r'^team/(?P<pk>[0-9]+)/membership/list/$', views.MembershipList.as_view(), name='membership.list'),
    # url(r'^team/(?P<team_pk>[0-9]+)/membership/(?P<pk>[0-9]+)/$', views.MembershipDetail.as_view(), name='membership.detail'),
    url(r'^team/(?P<team_pk>[0-9]+)/membership/(?P<pk>[0-9]+)/update/$', views.MembershipUpdate.as_view(), name='membership.update'),
    # url(r'^team/(?P<team_pk>[0-9]+)/membership/(?P<pk>[0-9]+)/delete/$', views.MembershipDelete.as_view(), name='membership.delete'),
    url(r'^team/(?P<pk>[0-9]+)/comment/create/$', views.CommentCreate.as_view(), name='comment.create'),
    url(r'^team/(?P<team_pk>[0-9]+)/comment/(?P<pk>[0-9]+)/delete/$', views.CommentDelete.as_view(), name='comment.delete'),
]

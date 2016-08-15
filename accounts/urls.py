from django.conf.urls import url
from django.contrib import auth

from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^update/$', views.update, name='update'),
    url(r'^search/$', views.search, name='search'),
    # url(r'^(?P<username>\w+)/$', views.detail, name='detail'),
    url(r'^join/(?P<username>\w+)/$', views.join_group, name='join'),
    url(r'^groups/(?P<username>\w+)/$', views.groups, name='groups'),
    url(r'^password_change/', views.password_change, name='password_change'),
    #url(r'^password/reset/$', auth.views.password_reset, {'post_reset_redirect': '/password/reset/done/'}, name='password_reset'),
    #url(r'^password/reset/done/$', auth.views.password_reset_done),
    #url(r'^password/reset/(?P<uid36>[0-9A-Za-z]+)-(?P<token>.+)/$', auth.views.password_reset_confirm, {'post_reset_redirect': '/password/done/'}, name='password_reset_confirm'),
    #url(r'^password/done/$', auth.views.password_reset_complete),
    url(r'^friend/(?P<username>\w+)/list/$', views.FriendList.as_view(), name='friend.list'),
    url(r'^friend/(?P<username>\w+)/for_list/$', views.FriendForList.as_view(), name='friend.list_for'),
    url(r'^friend/(?P<username>\w+)/create/$', views.FriendCreate.as_view(), name='friend.create'),
    url(r'^friend/(?P<username>\w+)/(?P<pk>[0-9]+)/$', views.FriendDetail.as_view(), name='friend.detail'),
    url(r'^friend/(?P<username>\w+)/(?P<pk>[0-9]+)/update/$', views.FriendUpdate.as_view(), name='friend.update'),
    url(r'^friend/(?P<username>\w+)/(?P<pk>[0-9]+)/delete/$', views.FriendDelete.as_view(), name='friend.delete'),
    url(r'^profile/list/$', views.ProfileList.as_view(), name='profile.list'),
    url(r'^profile/(?P<username>\w+)/$', views.ProfileDetail.as_view(), name='profile.detail'),
    url(r'^profile/(?P<username>\w+)/update/$', views.ProfileUpdate.as_view(), name='profile.update'),
    url(r'^profile/(?P<username>\w+)/friend/$', views.profile_toggle_friend, name='profile.friend'),
    url(r'^profile/(?P<username>\w+)/credit/$', views.profile_toggle_credit, name='profile.credit'),
]


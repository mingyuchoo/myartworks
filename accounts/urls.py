from django.urls import path
from django.contrib import auth

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('search/', views.search, name='search'),
    #path('<username>/', views.detail, name='detail'),
    path('join/<username>/', views.join_group, name='join'),
    path('groups/<username>/', views.groups, name='groups'),
    path('password_change/', views.password_change, name='password_change'),
    #path('password/reset/', auth.views.password_reset, {'post_reset_redirect': '/password/reset/done/'}, name='password_reset'),
    #path('password/reset/done/', auth.views.password_reset_done),
    #path('password/reset/<uid36>[0-9A-Za-z]+)-<token>.+)/', auth.views.password_reset_confirm, {'post_reset_redirect': '/password/done/'}, name='password_reset_confirm'),
    #path('password/done/', auth.views.password_reset_complete),
    path('friend/<username>/list/', views.FriendList.as_view(), name='friend.list'),
    path('friend/<username>/for_list/', views.FriendForList.as_view(), name='friend.list_for'),
    path('friend/<username>/create/', views.FriendCreate.as_view(), name='friend.create'),
    path('friend/<username>/<pk>/', views.FriendDetail.as_view(), name='friend.detail'),
    path('friend/<username>/<pk>/update/', views.FriendUpdate.as_view(), name='friend.update'),
    path('friend/<username>/<pk>/delete/', views.FriendDelete.as_view(), name='friend.delete'),
    path('profile/list/', views.ProfileList.as_view(), name='profile.list'),
    path('profile/<username>/', views.ProfileDetail.as_view(), name='profile.detail'),
    path('profile/<username>/update/', views.ProfileUpdate.as_view(), name='profile.update'),
    path('profile/<username>/friend/', views.profile_toggle_friend, name='profile.friend'),
    path('profile/<username>/credit/', views.profile_toggle_credit, name='profile.credit'),
]


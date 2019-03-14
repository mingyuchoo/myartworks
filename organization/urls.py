from django.urls import path

from . import views


app_name = 'organization'

urlpatterns = [
    path('team/tile/', views.TeamTile.as_view(), name='team.tile'),
    path('team/user/', views.TeamUser.as_view(), name='team.user'),
    path('team/create/', views.TeamCreate.as_view(), name='team.create'),
    path('team/<pk>/', views.TeamDetail.as_view(), name='team.detail'),
    path('team/<pk>/update/', views.TeamUpdate.as_view(), name='team.update'),
    path('team/<pk>/delete/', views.TeamDelete.as_view(), name='team.delete'),
    path('team/<pk>/bookmark/', views.team_toggle_bookmark, name='team.bookmark'),
    path('team/<pk>/apply/', views.team_toggle_apply, name='team.apply'),
    path('team/<pk>/share/', views.team_toggle_share, name='team.share'),
    # path('team/<pk>/membership/list/', views.MembershipList.as_view(), name='membership.list'),
    # path('team/<team_pk>/membership/<pk>/', views.MembershipDetail.as_view(), name='membership.detail'),
    path('team/<team_pk>/membership/<pk>/update/', views.MembershipUpdate.as_view(), name='membership.update'),
    # path('team/<team_pk>/membership/<pk>/delete/', views.MembershipDelete.as_view(), name='membership.delete'),
    path('team/<pk>/comment/create/', views.CommentCreate.as_view(), name='comment.create'),
    path('team/<team_pk>/comment/<pk>/delete/', views.CommentDelete.as_view(), name='comment.delete'),
]

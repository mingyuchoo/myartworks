from django.urls import path

from . import views

app_name = 'group'

urlpatterns = [
    path('project/tile/', views.ProjectTile.as_view(), name='project.tile'),
    path('project/user/', views.ProjectUser.as_view(), name='project.user'),
    path('project/create/', views.ProjectCreate.as_view(), name='project.create'),
    path('project/<pk>/', views.ProjectDetail.as_view(), name='project.detail'),
    path('project/<pk>/update/', views.ProjectUpdate.as_view(), name='project.update'),
    path('project/<pk>/delete/', views.ProjectDelete.as_view(), name='project.delete'),
    path('project/<pk>/bookmark/', views.project_toggle_bookmark, name='project.bookmark'),
    path('project/<pk>/apply/', views.project_toggle_apply, name='project.apply'),
    path('project/<pk>/share/', views.project_toggle_share, name='project.share'),
    # path('project/<pk>/membership/list/', views.MembershipList.as_view(), name='membership.list'),
    # path('project/<project_pk>/membership/<pk>/', views.MembershipDetail.as_view(), name='membership.detail'),
    path('project/<project_pk>/membership/<pk>/update/', views.MembershipUpdate.as_view(), name='membership.update'),
    # path('project/<project_pk>/membership/<pk>/delete/', views.MembershipDelete.as_view(), name='membership.delete'),
    path('project/<pk>/comment/create/', views.CommentCreate.as_view(), name='comment.create'),
    path('project/<project_pk>/comment/<pk>/delete/', views.CommentDelete.as_view(), name='comment.delete'),
]

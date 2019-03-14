from django.urls import path

from . import views

app_name = 'job'

urlpatterns = [
    path('', views.index, name='index'),
    path('work/tile/', views.WorkTile.as_view(), name='work.tile'),
    path('work/user/', views.WorkUser.as_view(), name='work.user'),
    path('work/create/', views.WorkCreate.as_view(), name='work.create'),
    path('work/<pk>/', views.WorkDetail.as_view(), name='work.detail'),
    path('work/<pk>/update/', views.WorkUpdate.as_view(), name='work.update'),
    path('work/<pk>/delete/', views.WorkDelete.as_view(), name='work.delete'),
    path('portfolio/<pk>/friend/', views.work_toggle_friend, name='work.friend'),
    path('portfolio/<pk>/bookmark/', views.work_toggle_bookmark, name='work.bookmark'),
    path('portfolio/<pk>/apply/', views.work_toggle_apply, name='work.apply'),
    path('portfolio/<pk>/share/', views.work_toggle_share, name='work.share'),
    path('work/<pk>/comment/create/', views.CommentCreate.as_view(), name='comment.create'),
    path('work/<work_pk>/comment/<pk>/delete/', views.CommentDelete.as_view(), name='comment.delete'),
]

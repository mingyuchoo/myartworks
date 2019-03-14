from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('<section>', views.index, name='index'),
    path('<section>/post/list/', views.PostList.as_view(), name='post.list'),
    path('<section>/post/create/', views.PostCreate.as_view(), name='post.create'),
    path('<section>/post/<pk>/', views.PostDetail.as_view(), name='post.detail'),
    path('<section>/post/<pk>/update/', views.PostUpdate.as_view(), name='post.update'),
    path('<section>/post/<pk>/delete/', views.PostDelete.as_view(), name='post.delete'),
    path('<section>/post/<pk>/comment/create/', views.CommentCreate.as_view(), name='comment.create'),
    path('<section>/post/<post_pk>/comment/<pk>/delete/', views.CommentDelete.as_view(), name='comment.delete'),
]

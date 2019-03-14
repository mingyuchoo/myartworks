from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('message/list/', views.MessageList.as_view(), name='message.list'),
    path('message/create/', views.MessageSend.as_view(), name='message.send'),
    path('message/<pk>/', views.MessageDetail.as_view(), name='message.read'),
    path('message/<pk>/reply/', views.MessageReply.as_view(), name='message.reply'),
    path('message/<pk>/archive/', views.MessageArchive.as_view(), name='message.archive'),
    path('message/<pk>/delete/', views.MessageDelete.as_view(), name='message.delete'),
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^message/list/$', views.MessageList.as_view(), name='message.list'),
    url(r'^message/create/$', views.MessageSend.as_view(), name='message.send'),
    url(r'^message/(?P<pk>[0-9]+)/$', views.MessageDetail.as_view(), name='message.read'),
    url(r'^message/(?P<pk>[0-9]+)/reply/$', views.MessageReply.as_view(), name='message.reply'),
    url(r'^message/(?P<pk>[0-9]+)/archive/$', views.MessageArchive.as_view(), name='message.archive'),
    url(r'^message/(?P<pk>[0-9]+)/delete/$', views.MessageDelete.as_view(), name='message.delete'),
]

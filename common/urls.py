from django.conf.urls import url

from . import views


app_name = 'common'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^contact/thanks/$', views.contact, name='thanks'),
    url(r'^privacy/$', views.privacy, name='privacy'),
    url(r'^terms/$', views.terms, name='terms'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^password_change/$', views.password_change, name='password_change'),
]
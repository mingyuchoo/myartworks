from django.conf.urls import url, include


from . import views

app_name = 'classification'

urlpatterns = [
    url(r'^category/list/$', views.CategoryList.as_view(), name='category.list'),
    url(r'^category/create/$', views.CategoryCreate.as_view(), name='category.create'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view(), name='category.detail'),
    url(r'^category/(?P<pk>[0-9]+)/update/$', views.CategoryUpdate.as_view(), name='category.update'),
    url(r'^category/(?P<pk>[0-9]+)/delete/$', views.CategoryDelete.as_view(), name='category.delete'),
    url(r'^field/list/$', views.FieldList.as_view(), name='field.list'),
    url(r'^field/create/$', views.FieldCreate.as_view(), name='field.create'),
    url(r'^field/(?P<pk>[0-9]+)/$', views.FieldDetail.as_view(), name='field.detail'),
    url(r'^field/(?P<pk>[0-9]+)/update/$', views.FieldUpdate.as_view(), name='field.update'),
    url(r'^field/(?P<pk>[0-9]+)/delete/$', views.FieldDelete.as_view(), name='field.delete'),
]

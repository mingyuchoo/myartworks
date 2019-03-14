from django.urls import path
from . import views


app_name = 'common'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact/thanks/', views.contact, name='thanks'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('logout/', views.logout, name='logout'),
    path('password_change/', views.password_change, name='password_change'),
]
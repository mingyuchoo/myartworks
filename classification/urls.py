from django.urls import path

from . import views

app_name = 'classification'

urlpatterns = [
    path('category/list/', views.CategoryList.as_view(), name='category.list'),
    path('category/create/', views.CategoryCreate.as_view(), name='category.create'),
    path('category/<pk>/', views.CategoryDetail.as_view(), name='category.detail'),
    path('category/<pk>/update/', views.CategoryUpdate.as_view(), name='category.update'),
    path('category/<pk>/delete/', views.CategoryDelete.as_view(), name='category.delete'),
    path('field/list/', views.FieldList.as_view(), name='field.list'),
    path('field/create/', views.FieldCreate.as_view(), name='field.create'),
    path('field/<pk>/', views.FieldDetail.as_view(), name='field.detail'),
    path('field/<pk>/update/', views.FieldUpdate.as_view(), name='field.update'),
    path('field/<pk>/delete/', views.FieldDelete.as_view(), name='field.delete'),
]

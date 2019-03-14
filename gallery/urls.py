from django.urls import path

from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/tile/', views.PortfolioTile.as_view(), name='portfolio.tile'),
    path('portfolio/user/', views.PortfolioUser.as_view(), name='portfolio.user'),
    path('portfolio/create_user/', views.PortfolioCreate.as_view(), name='portfolio.create'),
    path('portfolio/create_project/<project_pk>/', views.PortfolioCreateForProject.as_view(), name='portfolio.create_for_project'),
    path('portfolio/create_team/<team_pk>/', views.PortfolioCreateForTeam.as_view(), name='portfolio.create_for_team'),
    path('portfolio/create_work/<work_pk>/', views.PortfolioCreateForWork.as_view(), name='portfolio.create_for_work'),
    path('portfolio/<pk>/', views.PortfolioDetail.as_view(), name='portfolio.detail'),
    path('portfolio/<pk>/update/', views.PortfolioUpdate.as_view(), name='portfolio.update'),
    path('portfolio/<pk>/friend/', views.portfolio_toggle_friend, name='portfolio.friend'),
    path('portfolio/<pk>/like/', views.portfolio_toggle_like, name='portfolio.like'),
    path('portfolio/<pk>/share/', views.portfolio_toggle_share, name='portfolio.share'),
    path('portfolio/<pk>/report/', views.portfolio_report, name='portfolio.report'),
    path('portfolio/<pk>/delete/', views.PortfolioDelete.as_view(), name='portfolio.delete'),
    path('portfolio/<pk>/comment/create/', views.CommentCreate.as_view(), name='comment.create'),
    path('portfolio/<portfolio_pk>/comment/<pk>/delete/', views.CommentDelete.as_view(), name='comment.delete'),
]

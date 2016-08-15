from django.conf.urls import url, include

from . import views

app_name = 'gallery'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^portfolio/tile/$', views.PortfolioTile.as_view(), name='portfolio.tile'),
    url(r'^portfolio/user/$', views.PortfolioUser.as_view(), name='portfolio.user'),
    url(r'^portfolio/create_user/$', views.PortfolioCreate.as_view(), name='portfolio.create'),
    url(r'^portfolio/create_project/(?P<project_pk>[0-9]+)/$', views.PortfolioCreateForProject.as_view(), name='portfolio.create_for_project'),
    url(r'^portfolio/create_team/(?P<team_pk>[0-9]+)/$', views.PortfolioCreateForTeam.as_view(), name='portfolio.create_for_team'),
    url(r'^portfolio/create_work/(?P<work_pk>[0-9]+)/$', views.PortfolioCreateForWork.as_view(), name='portfolio.create_for_work'),
    url(r'^portfolio/(?P<pk>[0-9]+)/$', views.PortfolioDetail.as_view(), name='portfolio.detail'),
    url(r'^portfolio/(?P<pk>[0-9]+)/update/$', views.PortfolioUpdate.as_view(), name='portfolio.update'),
    url(r'^portfolio/(?P<pk>[0-9]+)/friend/$', views.portfolio_toggle_friend, name='portfolio.friend'),
    url(r'^portfolio/(?P<pk>[0-9]+)/like/$', views.portfolio_toggle_like, name='portfolio.like'),
    url(r'^portfolio/(?P<pk>[0-9]+)/share/$', views.portfolio_toggle_share, name='portfolio.share'),
    url(r'^portfolio/(?P<pk>[0-9]+)/report/$', views.portfolio_report, name='portfolio.report'),
    url(r'^portfolio/(?P<pk>[0-9]+)/delete/$', views.PortfolioDelete.as_view(), name='portfolio.delete'),
    url(r'^portfolio/(?P<pk>[0-9]+)/comment/create/$', views.CommentCreate.as_view(), name='comment.create'),
    url(r'^portfolio/(?P<portfolio_pk>[0-9]+)/comment/(?P<pk>[0-9]+)/delete/$', views.CommentDelete.as_view(), name='comment.delete'),
]

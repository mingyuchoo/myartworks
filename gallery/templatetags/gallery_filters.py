from django import template
from django.contrib.auth.models import User
from gallery.models import Portfolio, Comment, Like, Share

register = template.Library()


@register.simple_tag(name='is_portfolio_friend')
def is_portfolio_friend(portfolio, *args, **kwargs):
    try:
        request_user = User.objects.get(username=kwargs["username"])
        return 'fa fa-link' if request_user.accounts_friends.filter(friend=portfolio.writer) else 'fa fa-chain-broken'
    except User.DoesNotExist:
        return 'fa fa-chain-broken'


@register.simple_tag(name='has_portfolio_comment')
def has_portfolio_comment(portfolio, *args, **kwargs):
    try:
        request_user = User.objects.get(username=kwargs["username"])
        comment = Comment.objects.filter(portfolio=portfolio, writer=request_user)
        return 'fa fa-commenting' if comment else 'fa fa-commenting-o'
    except User.DoesNotExist or Comment.DoesNotExist:
        return 'fa fa-commenting-o'


@register.simple_tag(name='has_portfolio_like')
def has_portfolio_like(portfolio, *args, **kwargs):
    try:
        request_user = User.objects.get(username=kwargs["username"])
        like = Like.objects.filter(portfolio=portfolio, writer=request_user)
        return 'fa fa-heart' if like else 'fa fa-heart-o'
    except User.DoesNotExist or Like.DoesNotExist:
        return 'fa fa-heart-o'


@register.simple_tag(name='has_portfolio_share')
def has_portfolio_share(portfolio, *args, **kwargs):
    try:
        request_user = User.objects.get(username=kwargs["username"])
        share = Share.objects.filter(portfolio=portfolio, writer=request_user)
        return 'fa fa-share-square' if share else 'fa fa-share-square-o'
    except User.DoesNotExist or Share.DoesNotExist:
        return 'fa fa-share-square-o'

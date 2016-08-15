from django import template
from django.contrib.auth.models import User

from organization.models import Comment, Bookmark, Apply, Share

register = template.Library()


@register.simple_tag(name='has_team_comment')
def has_team_comment(team, *args, **kwargs):
    try:
        request_user = User.objects.get(username=kwargs["username"])
        comment = Comment.objects.filter(team=team, writer=request_user)
        return 'fa fa-commenting' if comment else 'fa fa-commenting-o'
    except User.DoesNotExist or Comment.DoesNotExist:
        return 'fa fa-commenting-o'


@register.simple_tag(name='has_team_bookmark')
def has_team_bookmark(team, *args, **kwargs):
    try:
        request_user = User.objects.get(username=kwargs["username"])
        bookmark = Bookmark.objects.filter(team=team, writer=request_user)
        return 'fa fa-bookmark' if bookmark else 'fa fa-bookmark-o'
    except User.DoesNotExist or Bookmark.DoesNotExist:
        return 'fa fa-bookmark-o'


@register.simple_tag(name='has_team_apply')
def has_team_apply(team, *args, **kwargs):
    try:
        request_user = User.objects.get(username=kwargs["username"])
        apply = Apply.objects.filter(team=team, writer=request_user)
        return 'fa fa-flag' if apply else 'fa fa-flag-o'
    except User.DoesNotExist or Apply.DoesNotExist:
        return 'fa fa-flag-o'


@register.simple_tag(name='has_team_share')
def has_team_share(team, *args, **kwargs):
    try:
        request_user = User.objects.get(username=kwargs["username"])
        share = Share.objects.filter(team=team, writer=request_user)
        return 'fa fa-share-square' if share else 'fa fa-share-square-o'
    except User.DoesNotExist or Share.DoesNotExist:
        return 'fa fa-share-square-o'

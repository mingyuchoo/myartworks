from django import template
from django.contrib.auth.models import User

from job.models import Comment, Bookmark, Apply, Share

register = template.Library()


@register.simple_tag(name='is_friend')
def is_friend(work, *args, **kwargs):
    try:
        request_user = User.objects.get(username=kwargs["username"])
        return 'fa fa-link' if request_user.accounts_friends.filter(friend=work.writer) else 'fa fa-chain-broken'
    except User.DoesNotExist:
        return 'fa fa-chain-broken'


@register.simple_tag(name='has_work_comment')
def has_work_comment(work, *args, **kwargs):
    try:
        request_user = User.objects.get(username=kwargs["username"])
        comment = Comment.objects.filter(work=work, writer=request_user)
        return 'fa fa-commenting' if comment else 'fa fa-commenting-o'
    except User.DoesNotExist or Comment.DoesNotExist:
        return 'fa fa-commenting-o'


@register.simple_tag(name='has_work_bookmark')
def has_work_bookmark(work, *args, **kwargs):
    try:
        request_user = User.objects.get(username=kwargs["username"])
        bookmark = Bookmark.objects.filter(work=work, writer=request_user)
        return 'fa fa-bookmark' if bookmark else 'fa fa-bookmark-o'
    except User.DoesNotExist or Bookmark.DoesNotExist:
        return 'fa fa-bookmark-o'


@register.simple_tag(name='has_work_apply')
def has_work_apply(work, *args, **kwargs):
    try:
        request_user = User.objects.get(username=kwargs["username"])
        apply = Apply.objects.filter(work=work, writer=request_user)
        return 'fa fa-flag' if apply else 'fa fa-flag-o'
    except User.DoesNotExist or Apply.DoesNotExist:
        return 'fa fa-flag-o'


@register.simple_tag(name='has_work_share')
def has_work_share(work, *args, **kwargs):
    try:
        request_user = User.objects.get(username=kwargs["username"])
        share = Share.objects.filter(work=work, writer=request_user)
        return 'fa fa-share-square' if share else 'fa fa-share-square-o'
    except User.DoesNotExist or Share.DoesNotExist:
        return 'fa fa-share-square-o'

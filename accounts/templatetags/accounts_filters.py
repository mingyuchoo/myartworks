from django import template
from django.contrib.auth.models import User
from accounts.models import Profile, Friend, Credit

register = template.Library()


@register.simple_tag(name='is_profile_friend')
def is_profile_friend(profile, *args, **kwargs):
    try:
        request_user = User.objects.get(username=kwargs["username"])
        return 'fa fa-link' if request_user.accounts_friends.filter(friend=profile.writer) else 'fa fa-chain-broken'
    except User.DoesNotExist:
        return 'fa fa-chain-broken'


@register.simple_tag(name='has_profile_credit')
def has_profile_credit(profile, *args, **kwargs):
    try:
        request_user = User.objects.get(username=kwargs["username"])
        credit = Credit.objects.filter(profile=profile, writer=request_user)
        return 'fa fa-star' if credit else 'fa fa-star-o'
    except User.DoesNotExist or Credit.DoesNotExist:
        return 'fa fa-star-o'


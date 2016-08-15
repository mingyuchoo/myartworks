from django import template
from django.contrib.auth.models import User

from blog.models import Post, Comment

register = template.Library()


@register.simple_tag(name='has_post_comment')
def has_post_comment(post, *args, **kwargs):
    try:
        request_user = User.objects.get(username=kwargs["username"])
        comment = Comment.objects.filter(post=post, writer=request_user)
        return 'fa fa-commenting' if comment else 'fa fa-commenting-o'
    except User.DoesNotExist or Comment.DoesNotExist:
        return 'fa fa-commenting-o'

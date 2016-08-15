import time
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Section(models.Model):
    """
    Section class for Blog
    """
    name = models.CharField(max_length=50)
    writer = models.ForeignKey(User, related_name='blog_sections')
    created_time = models.DateTimeField(default=timezone.now)
    updated_time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = [
            '-created_time'
        ]

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Post class
    """
    section = models.ForeignKey(Section)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=''.join(['blog/', time.strftime('%Y%m%d'), '/']), blank=True, null=True)
    content = models.CharField(max_length=200)
    writer = models.ForeignKey(User, related_name='blog_posts')
    created_time = models.DateTimeField(default=timezone.now)
    updated_time = models.DateTimeField(default=timezone.now)

    class Meta:
        permissions = [
            ['view_post', 'Can view post'],
        ]
        ordering = [
            '-created_time'
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post.list')

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    """
    Comment class
    """
    post = models.ForeignKey(Post)
    content = models.CharField(max_length=200)
    writer = models.ForeignKey(User, related_name='blog_comments')
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        permissions = [
            ['view_comment', 'Can view comment'],
        ]
        ordering = [
            '-created_time'
        ]

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('blog:post.detail', kwargs={'pk': str(self.post.pk)})

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)

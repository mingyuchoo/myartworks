import time
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from classification.models import Category
from group.models import Project
from organization.models import Team

from taggit.managers import TaggableManager

class Work(models.Model):
    """
    Work class
    """
    image = models.ImageField(upload_to=''.join(['job/', time.strftime('%Y%m%d'), '/']))
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=2048)
    category = models.ManyToManyField(Category)
    writer = models.ForeignKey(User, null=True)
    team = models.ForeignKey(Team, null=True)
    project = models.ForeignKey(Project, null=True)
    created_time = models.DateTimeField(default=timezone.now)
    updated_time = models.DateTimeField(default=timezone.now)
    comment_count = models.IntegerField(default=0)
    bookmark_count = models.IntegerField(default=0)
    apply_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    tags = TaggableManager()

    class Meta:
        permissions = [
            ['view_work', 'Can view work'],
        ]

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('job:work.tile')

    def categories(self):
        return ", ".join([category.name for category in self.category.all()])


class Comment(models.Model):
    """
    Comment class
    """
    work = models.ForeignKey(Work)
    content = models.CharField(max_length=200)
    writer = models.ForeignKey(User, related_name='work_comments')
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        permissions = [
            ['view_comment', 'Can view comment'],
        ]

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('job:work.detail', kwargs={'pk': str(self.work.pk)})

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)


class Bookmark(models.Model):
    """
    Bookmark class
    """
    work = models.ForeignKey(Work)
    writer = models.ForeignKey(User, related_name='work_bookmarks')
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        permissions = [
            ['view_bookmark', 'Can view bookmark'],
        ]

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('job:work.detail', kwargs={'pk': str(self.work.pk)})

    def save(self, *args, **kwargs):
        super(Bookmark, self).save(*args, **kwargs)


class Apply(models.Model):
    """
    Apply class
    """
    work = models.ForeignKey(Work)
    writer = models.ForeignKey(User, related_name='work_applies')
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        permissions = [
            ['view_apply', 'Can view apply'],
        ]

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('job:work.detail', kwargs={'pk': str(self.work.pk)})

    def save(self, *args, **kwargs):
        super(Apply, self).save(*args, **kwargs)


class Share(models.Model):
    """
    Share class
    """
    work = models.ForeignKey(Work)
    writer = models.ForeignKey(User, related_name='work_shares')
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        permissions = [
            ['view_share', 'Can view share'],
        ]

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('job:work.detail', kwargs={'pk': str(self.work.pk)})

    def save(self, *args, **kwargs):
        super(Share, self).save(*args, **kwargs)

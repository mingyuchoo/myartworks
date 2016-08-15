import time
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from classification.models import Category
from group.models import Project
from organization.models import Team
from job.models import Work

from taggit.managers import TaggableManager


class Portfolio(models.Model):
    """
    Portfolio class
    """
    image = models.ImageField(upload_to=''.join(['gallery/', time.strftime('%Y%m%d'), '/']))
    resource = models.FileField(upload_to='gallery/resource/', blank=True, null=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    writer = models.ForeignKey(User, null=True)
    project = models.ForeignKey(Project, null=True)
    team = models.ForeignKey(Team, null=True)
    work = models.ForeignKey(Work, null=True)
    created_time = models.DateTimeField(default=timezone.now)
    updated_time = models.DateTimeField(default=timezone.now)
    comment_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    report_count = models.IntegerField(default=0)
    tags = TaggableManager()

    class Meta:
        permissions = [
            ['view_portfolio', 'Can view portfolio'],
        ]

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('gallery:portfolio.tile')

    def categories(self):
        return ", ".join([category.name for category in self.category.all()])


class Comment(models.Model):
    """
    Comment class
    """
    portfolio = models.ForeignKey(Portfolio)
    content = models.CharField(max_length=200)
    writer = models.ForeignKey(User, related_name='gallery_comments')
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        permissions = [
            ['view_comment', 'Can view comment'],
        ]

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('gallery:portfolio.detail', kwargs={'pk': str(self.portfolio.pk)})

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)


class Like(models.Model):
    """
    Like class
    """
    portfolio = models.ForeignKey(Portfolio)
    writer = models.ForeignKey(User, related_name='gallery_likes')
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        permissions = [
            ['view_like', 'Can view like'],
        ]

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('gallery:portfolio.detail', kwargs={'pk': str(self.portfolio.pk)})


class Share(models.Model):
    """
    Share class
    """
    portfolio = models.ForeignKey(Portfolio)
    writer = models.ForeignKey(User, related_name='gallery_shares')
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        permissions = [
            ['view_share', 'Can view share'],
        ]

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('gallery:portfolio.detail', kwargs={'pk': str(self.portfolio.pk)})

    def save(self, *args, **kwargs):
        super(Share, self).save(*args, **kwargs)


class Report(models.Model):
    """
    Report class
    """
    portfolio = models.ForeignKey(Portfolio)
    writer = models.ForeignKey(User, related_name='gallery_reports')
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        permissions = [
            ['view_report', 'Can view report'],
        ]

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('gallery:portfolio.detail', kwargs={'pk': str(self.portfolio.pk)})

    def save(self, *args, **kwargs):
        super(Report, self).save(*args, **kwargs)

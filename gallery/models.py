import time
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
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
    writer = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    work = models.ForeignKey(Work, null=True, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    report_count = models.IntegerField(default=0)
    tags = TaggableManager()

    class Meta:
        pass

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
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    writer = models.ForeignKey(User, related_name='gallery_comments', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

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
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, related_name='gallery_likes', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('gallery:portfolio.detail', kwargs={'pk': str(self.portfolio.pk)})


class Share(models.Model):
    """
    Share class
    """
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, related_name='gallery_shares', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

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
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, related_name='gallery_reports', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('gallery:portfolio.detail', kwargs={'pk': str(self.portfolio.pk)})

    def save(self, *args, **kwargs):
        super(Report, self).save(*args, **kwargs)

import time
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
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
    writer = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=timezone.now)
    updated_time = models.DateTimeField(default=timezone.now)
    comment_count = models.IntegerField(default=0)
    bookmark_count = models.IntegerField(default=0)
    apply_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    tags = TaggableManager()

    class Meta:
        pass

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
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    writer = models.ForeignKey(User, related_name='work_comments', on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        pass

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
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, related_name='work_bookmarks', on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        pass

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
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, related_name='work_applies', on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        pass

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
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, related_name='work_shares', on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        pass

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('job:work.detail', kwargs={'pk': str(self.work.pk)})

    def save(self, *args, **kwargs):
        super(Share, self).save(*args, **kwargs)

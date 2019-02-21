from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from classification.models import Category
from organization.models import Team

from taggit.managers import TaggableManager

class Project(models.Model):
    """
    Project class
    """
    STATUS = (
        ('O', 'Open'),
        ('C', 'Closed'),
    )
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=5120)
    manager = models.ForeignKey(User, related_name='group_project_leaders', on_delete=models.CASCADE)
    member = models.ManyToManyField(User, through='Membership')
    status = models.CharField(max_length=1, choices=STATUS, default='O')
    writer = models.ForeignKey(User, related_name='group_projects', null=True, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=timezone.now)
    updated_time = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField(Category)
    comment_count = models.IntegerField(default=0)
    bookmark_count = models.IntegerField(default=0)
    apply_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    tags = TaggableManager()

    class Meta:
        pass

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('group:project.user')

    def categories(self):
        return ", ".join([category.name for category in self.category.all()])


class Membership(models.Model):
    """
    Membership class (Project-M2M-User)
    """
    STATUS = (
        ('R', 'Request'),
        ('D', 'Denied'),
        ('A', 'Approved'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_project_members')
    status = models.CharField(max_length=1, choices=STATUS, default='R')
    updated_time = models.DateTimeField(default=timezone.now)
    requested_date = models.DateTimeField(default=timezone.now)
    joined_date = models.DateTimeField(null=True)

    class Meta:
        pass

    def get_absolute_url(self):
        return reverse('group:project.detail', kwargs={'pk': str(self.project.pk)})

    def __str__(self):
        return "{}:{}-{}".format(self.id, self.project.name, self.member.username)


class Comment(models.Model):
    """
    Comment class
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    writer = models.ForeignKey(User, related_name='project_comments', on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        pass

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('group:project.detail', kwargs={'pk': str(self.project.pk)})

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)


class Bookmark(models.Model):
    """
    Bookmark class
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, related_name='project_bookmarks', on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        pass

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('group:project.detail', kwargs={'pk': str(self.project.pk)})

    def save(self, *args, **kwargs):
        super(Bookmark, self).save(*args, **kwargs)


class Apply(models.Model):
    """
    Apply class
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, related_name='project_applies', on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        pass

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('group:project.detail', kwargs={'pk': str(self.project.pk)})

    def save(self, *args, **kwargs):
        super(Apply, self).save(*args, **kwargs)


class Share(models.Model):
    """
    Share class
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, related_name='project_shares', on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        pass

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('group:project.detail', kwargs={'pk': str(self.project.pk)})

    def save(self, *args, **kwargs):
        super(Share, self).save(*args, **kwargs)


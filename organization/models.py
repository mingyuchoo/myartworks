from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from classification.models import Category

from taggit.managers import TaggableManager


class Team(models.Model):
    """
    Team class
    """
    STATUS = (
        ('O', 'Open'),
        ('C', 'Closed'),
    )
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=5120)
    leader = models.ForeignKey(User, related_name='organization_team_leaders', on_delete=models.DO_NOTHING)
    member = models.ManyToManyField(User, through='Membership')
    status = models.CharField(max_length=1, choices=STATUS, default='O')
    writer = models.ForeignKey(User, related_name='organization_teams', on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)
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
        return reverse('organization:team.user')

    def categories(self):
        return ", ".join([category.name for category in self.category.all()])


class Membership(models.Model):
    """
    Membership class (Team-M2M-User)
    """
    STATUS = (
        ('R', 'Request'),
        ('D', 'Denied'),
        ('A', 'Approved'),
    )
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING)
    member = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='organization_team_members')
    status = models.CharField(max_length=1, choices=STATUS, default='R')
    updated_time = models.DateTimeField(auto_now_add=True)
    requested_date = models.DateField(auto_now_add=True)
    joined_date = models.DateField(null=True)

    class Meta:
        pass

    def get_absolute_url(self):
        return reverse('organization:team.detail', kwargs={'pk': str(self.team.pk)})

    def __str__(self):
        return "{}:{}-{}".format(self.id, self.team.name, self.member.username)


class Comment(models.Model):
    """
    Comment class
    """
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    writer = models.ForeignKey(User, related_name='team_comments', on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('organization:team.detail', kwargs={'pk': str(self.team.pk)})

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)


class Bookmark(models.Model):
    """
    Bookmark class
    """
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, related_name='team_bookmarks', on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('organization:team.detail', kwargs={'pk': str(self.team.pk)})

    def save(self, *args, **kwargs):
        super(Bookmark, self).save(*args, **kwargs)


class Apply(models.Model):
    """
    Apply class
    """
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, related_name='team_applies', on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('organization:team.detail', kwargs={'pk': str(self.team.pk)})

    def save(self, *args, **kwargs):
        super(Apply, self).save(*args, **kwargs)


class Share(models.Model):
    """
    Share class
    """
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, related_name='team_shares', on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('organization:team.detail', kwargs={'pk': str(self.team.pk)})

    def save(self, *args, **kwargs):
        super(Share, self).save(*args, **kwargs)


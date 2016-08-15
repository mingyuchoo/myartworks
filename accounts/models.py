import uuid, time
from django.utils import timezone
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from taggit.managers import TaggableManager


class Profile(models.Model):
    GENDER = (
        ('M', _('Male')),
        ('F', _('Female')),
    )
    STATUS = (
        ('A', _('Available')),
        ('O', _('Occupied')),
    )
    TYPE = (
        ('P', _('Personal')),
        ('C', _('Company')),
        ('G', _('Government')),
    )
    writer = models.OneToOneField(User, primary_key=True)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    picture = models.ImageField('Profile picture',
                                upload_to=''.join(['profile_picture/', time.strftime('%Y%m%d'), '/']),
                                default='profile_picture/default.png',
                                blank=True,
                                null=True
                                )
    nick_name = models.CharField(max_length=128)
    gender = models.CharField(max_length=1, choices=GENDER, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=128, blank=True, null=True)
    bio = models.TextField("Bio", max_length=2048, blank=True, null=True)
    status = models.CharField(max_length=1, default='A', choices=STATUS)
    type = models.CharField(max_length=1, default='P', choices=TYPE)
    credit_count = models.IntegerField(default=0)
    tags = TaggableManager()

    class Meta:
        permissions = [
            ['view_profile', 'Can view profile', ]
        ]

    def __str__(self):
        return self.writer.username


class Friend(models.Model):
    """
    Friend class
    """
    writer = models.ForeignKey(User, related_name="accounts_friends")
    friend = models.ForeignKey(User, related_name="accounts_friend_friends")
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        permissions = [
            ['view_friend', 'Can view friend'],
        ]

    def __str__(self):
        return "{}:{}->{}".format(self.id, self.writer.username, self.friend.username)

    def get_absolute_url(self):
        return reverse('accounts:friend.detail', kwargs={'pk': str(self.friend.pk)})


class Credit(models.Model):
    """
    Credit class
    """
    profile = models.ForeignKey(Profile)
    writer = models.ForeignKey(User, related_name='profile_credits')
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        permissions = [
            ['view_credit', 'Can view credit'],
        ]

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('accounts:credit.detail', kwargs={'pk': str(self.credit.pk)})

    def save(self, *args, **kwargs):
        super(Credit, self).save(*args, **kwargs)


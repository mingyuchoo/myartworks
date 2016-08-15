import time
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Category(models.Model):
    """
    Category class
    """
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', blank=True, null=True)
    writer = models.ForeignKey(User, related_name='classification_categories')
    created_time = models.DateTimeField(default=timezone.now)
    updated_time = models.DateTimeField(default=timezone.now)

    class Meta:
        permissions = [
            ['view_category', 'Can view category'],
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('classification:category.list')


class Field(models.Model):
    """
    Field class
    """
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', blank=True, null=True)
    writer = models.ForeignKey(User, related_name='classification_fields')
    created_time = models.DateTimeField(default=timezone.now)
    updated_time = models.DateTimeField(default=timezone.now)

    class Meta:
        permissions = [
            ['view_field', 'Can view field'],
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('classification:field.list')

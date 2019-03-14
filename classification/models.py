from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    """
    Category class
    """
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, related_name='classification_categories', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('classification:category.list')


class Field(models.Model):
    """
    Field class
    """
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, related_name='classification_fields', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('classification:field.list')

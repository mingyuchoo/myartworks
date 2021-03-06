# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 01:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('group', '0001_initial'),
        ('gallery', '0001_initial'),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='group.Project'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 01:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classification', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'permissions': [['view_comment', 'Can view comment']],
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'permissions': [['view_like', 'Can view like']],
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/20160815/')),
                ('resource', models.FileField(blank=True, null=True, upload_to='gallery/resource/')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=200)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment_count', models.IntegerField(default=0)),
                ('like_count', models.IntegerField(default=0)),
                ('share_count', models.IntegerField(default=0)),
                ('report_count', models.IntegerField(default=0)),
                ('category', models.ManyToManyField(to='classification.Category')),
            ],
            options={
                'permissions': [['view_portfolio', 'Can view portfolio']],
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Portfolio')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_reports', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': [['view_report', 'Can view report']],
            },
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Portfolio')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_shares', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': [['view_share', 'Can view share']],
            },
        ),
    ]

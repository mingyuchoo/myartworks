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
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('organization', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'permissions': [['view_award', 'Can view award']],
            },
        ),
        migrations.CreateModel(
            name='Basic',
            fields=[
                ('writer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('full_name', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'permissions': [['view_basic', 'Can view basic']],
            },
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('details', models.CharField(max_length=5000)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'permissions': [['view_career', 'Can view career']],
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=50)),
                ('organization', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('acquisition_date', models.DateField()),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'permissions': [['view_certificate', 'Can view certificate']],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('writer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('email', models.CharField(max_length=50)),
                ('phone1', models.CharField(max_length=50)),
                ('phone2', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'permissions': [['view_contact', 'Can view contact']],
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('details', models.CharField(max_length=5000)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'permissions': [['view_education', 'Can view education']],
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=50)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'permissions': [['view_language', 'Can view language']],
            },
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('writer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('content', models.CharField(max_length=10000)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'permissions': [['view_letter', 'Can view letter']],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=50)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_skills', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': [['view_skill', 'Can view skill']],
            },
        ),
        migrations.AddField(
            model_name='language',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_languages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='education',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_educations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='certificate',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_certificates', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='career',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_careers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='award',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_awards', to=settings.AUTH_USER_MODEL),
        ),
    ]
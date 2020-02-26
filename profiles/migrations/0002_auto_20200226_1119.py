# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-26 11:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='followers',
        ),
        migrations.AlterField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='is_following', to=settings.AUTH_USER_MODEL),
        ),
    ]
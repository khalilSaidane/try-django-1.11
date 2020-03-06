# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-03-06 09:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='restaurants_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]

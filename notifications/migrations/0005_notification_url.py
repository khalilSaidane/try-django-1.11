# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-03-07 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_auto_20200306_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

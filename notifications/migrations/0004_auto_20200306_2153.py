# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-03-06 21:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_notification_is_read'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='action_object',
            new_name='content_type',
        ),
    ]

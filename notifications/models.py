# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
User = settings.AUTH_USER_MODEL


class Notification(models.Model):
    actor = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='notifications_actor')
    target = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='notifications_target')
    # The object that caused the notification
    action_object = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('action_object', 'object_id')
    verb = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


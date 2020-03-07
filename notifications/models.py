# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class NotificationManager(models.Manager):
    def save_notification_or_update_similar(self, notification):
        '''
            Make sure that notifications are unique
            and the timestamp correspond to the last time
            the event has occurred
        '''
        query = Notification.objects.filter(actor=notification.actor, target=notification.target,
                                            verb=notification.verb,
                                            url=notification.url)
        if query.exists():
            similar = query.first()
            similar.timestamp = timezone.now()
            similar.save()
            return similar
        else:
            notification.save()
            return notification


class Notification(models.Model):
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='notifications_actor')
    target = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                               related_name='notifications_target')
    # The object that caused the notification
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    verb = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    url = models.CharField(max_length=100, null=True)
    objects = NotificationManager()

    def __str__(self):
        return self.url

    class Meta:
        ordering = ['-timestamp']

    def get_read_notification_url(self):
        return reverse('notifications-api:update', kwargs={'pk': self.id})


from django.db.models.signals import m2m_changed
from profiles.models import Profile
from restaurents.models import Restaurant


def notify(verb, redirect_to_actor_profile=False):
    def notify_func(sender, instance, action, *args, **kwargs):
        if action == 'post_add':
            actor_id = [id for id in kwargs['pk_set']][0]
            actor = User.objects.get(id=actor_id)
            target = instance.user
            v = verb
            try:
                if redirect_to_actor_profile:
                    url = actor.profile.get_absolute_url()
                else:
                    url = instance.get_absolute_url()
            except:
                url = None
            # to avoid duplicate notifications
            notification = Notification(actor=actor, target=target, content_object=instance, verb=v, url=url)
            Notification.objects.save_notification_or_update_similar(notification)
    return notify_func


notify_on_follow = notify(verb='stated following you', redirect_to_actor_profile=True)
notify_on_like = notify(verb='liked your restaurant')

m2m_changed.connect(notify_on_follow, sender=Profile.followers.through)
m2m_changed.connect(notify_on_like, sender=Restaurant.likes.through)

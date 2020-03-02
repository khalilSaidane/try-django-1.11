# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.urls import reverse

User = settings.AUTH_USER_MODEL


class ProfileManager(models.Manager):
    def toggle_follow(self,request_user, username_to_toggle):
        profile_ = Profile.objects.get(user__username__iexact=username_to_toggle)
        user = request_user
        is_following = False
        if user in profile_.followers.all():
            profile_.followers.remove(user)
        else:
            profile_.followers.add(user)
            is_following = True
        return is_following, profile_


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    followers = models.ManyToManyField(User, related_name='is_following', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_activated = models.BooleanField(default=False)
    objects = ProfileManager()

    def __str__(self):
        return self.user.username

    def get_toggle_follow_url(self):
        return reverse('profiles:follow-api-toggle', kwargs={'username': self.user.username})


def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)
        default_user_profile = Profile.objects.get_or_create(user__id=1)[0]
        default_user_profile.followers.add(instance)
        profile.followers.add(default_user_profile.user)
        profile.followers.add(2)


post_save.connect(post_save_user_receiver, sender=User)

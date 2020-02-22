# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from restaurents.models import Restaurant
from django.urls import reverse


class Menu(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey(Restaurant)
    name = models.CharField(max_length=120)
    contents = models.TextField(help_text='Separate each item by comma')
    excludes = models.TextField(blank=True, null=True, help_text='Separate each item by comma')
    is_public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('menus:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-updated', '-timestamp']

    def get_contents(self):
        return self.contents.split(',')

    def get_excludes(self):
        return self.excludes.split(',')

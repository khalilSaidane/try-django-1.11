# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from .validators import validate_name
from django.conf import settings
from django.urls import reverse
from django.db.models import Q


class RestaurantQuerySet(models.query.QuerySet):
    def search(self, query):  # Restaurant.objects.all().search(query)      def search(self, query):  # Restaurant.objects.filter(something).search(query)
        if query:
            query = query.strip()
            return self.filter(Q(name__icontains=query) |
                               Q(location__icontains=query) |
                               Q(category__icontains=query) |
                               Q(menu__name__icontains=query) |
                               Q(menu__contents__icontains=query)
                               ).distinct()
        return self


class RestaurantManager(models.Manager):
    def get_queryset(self):
        return RestaurantQuerySet(self.model, using=self._db)

    def search(self, query):  # Restaurant.objects.search()
        return self.get_queryset().search(query)


class Restaurant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100, validators=[validate_name])
    location = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='restaurants_likes')
    objects = RestaurantManager()  # this will add the manager to objects

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('restaurants:detail', kwargs={'slug': self.slug})

    def get_toggle_like_url(self):
        return reverse('restaurants-api:toggle-like', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.name


def r_pre_save_receiver(sender, instance, *args, **kwargs):
    print('saving..')

    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(r_pre_save_receiver, sender=Restaurant)

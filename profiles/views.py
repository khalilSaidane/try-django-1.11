# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, View, CreateView
from django.contrib.auth import get_user_model
from django.http import Http404
from restaurents.models import Restaurant
from menus.models import Menu
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()


class ProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = 'profiles/user.html'

    def get_object(self):
        username = self.kwargs.get('username')
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)

    def get_context_data(self,*args, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
        user = context['user']
        is_following = False
        if user.profile in self.request.user.is_following.all():
            is_following = True
        context['is_following'] = is_following
        query = self.request.GET.get('q')
        menu_exists = Menu.objects.filter(user=user).exists()
        qs = Restaurant.objects.filter(user=user).search(query)
        if qs.exists() and menu_exists:
            context['restaurants'] = qs
        return context

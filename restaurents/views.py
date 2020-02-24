# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView
from .models import Restaurant
from django.db.models import Q
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import RestaurantForm


class RestaurantCreateView(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    form_class = RestaurantForm
    template_name = 'form.html'
    success_message = "Restaurant %(name)s is successfully created"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context


class RestaurantListView(LoginRequiredMixin, ListView):
    template_name = 'restaurants/restaurants_list.html'

    def get_queryset(self):
        return Restaurant.objects.filter(user=self.request.user)


class RestaurantDetailView(LoginRequiredMixin, DetailView):
    template_name = 'restaurants/restaurants_detail.html'

    def get_queryset(self):
        return Restaurant.objects.filter(user=self.request.user)


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = RestaurantForm

    def get_queryset(self):
        return Restaurant.objects.filter(user=self.request.user)

    def get_context_data(self,*args, **kwargs):
        context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Restaurant'
        return context

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Menu
from django.views import generic
from .forms import MenuForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


class MenuListView(generic.ListView):
    def get_queryset(self):
        return Menu.objects.filter(user=self.request.user)


class MenuDetailView(generic.DetailView):
    def get_queryset(self):
        return Menu.objects.filter(user=self.request.user)


class MenuCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = MenuForm
    template_name = 'form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(MenuCreateView, self).form_valid(form)

    def get_queryset(self):
        return Menu.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(MenuCreateView, self).get_context_data(*args,**kwargs)
        context['title'] = 'Add Menu'
        return context

    # The user argument will be sent to the form to ensure that the list of restaurants available are the ones that he created
    def get_form_kwargs(self):
        kwargs = super(MenuCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class MenuUpdateView(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    form_class = MenuForm
    template_name = 'menus/detail-update.html'
    success_message = "Menu %(name)s is successfully updated"

    def get_queryset(self):
        return Menu.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(MenuUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Menu'
        return context

    def get_form_kwargs(self):
        kwargs = super(MenuUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

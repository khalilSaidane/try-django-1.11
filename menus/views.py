# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Menu
from django.views import generic
from .forms import MenuForm


class MenuListView(generic.ListView):
    def get_queryset(self):
        return Menu.objects.filter(user=self.request.user)


class MenuDetailView(generic.DetailView):
    def get_queryset(self):
        return Menu.objects.filter(user=self.request.user)


class MenuCreateView(generic.CreateView):
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


class MenuUpdateView(generic.UpdateView):
    form_class = MenuForm

    def get_queryset(self):
        return Menu.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(MenuUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Menu'
        return context

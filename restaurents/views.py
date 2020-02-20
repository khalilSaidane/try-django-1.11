# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'home/home.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context = {
            'data': 'I am some data'
        }
        return context
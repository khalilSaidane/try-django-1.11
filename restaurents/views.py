# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.
def home(request):
    return render(request, 'home/home.html', {})


def about(request):
    return render(request, 'home/about.html', {})


def contact(request):
    return render(request, 'home/contact.html', {})

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Restaurant
from django.db.models import Q
from django.views import generic


class RestaurantCreateView(generic.CreateView):
    model = Restaurant
    fields = [
        'name',
        'location',
        'category'
        ]
    template_name = 'restaurants/form.html'
    success_url = '/restaurants'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)


def restaurants_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    queryset = Restaurant.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, template_name, context)


class RestaurantListView(ListView):
    template_name = 'restaurants/restaurants_list.html'
    queryset = Restaurant.objects.all()

    def get_queryset(self):
        print(self.kwargs)
        slug = self.kwargs.get('slug')
        if slug:
            queryset = Restaurant.objects.filter(category__icontains=slug)
        else:
            queryset = Restaurant.objects.all()
        return queryset


class RestaurantDetailView(DetailView):
    queryset = Restaurant.objects.all()
    template_name = 'restaurants/restaurants_detail.html'

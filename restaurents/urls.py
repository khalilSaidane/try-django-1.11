from django.conf.urls import url
from . import views
from django.views.generic import TemplateView



urlpatterns = [
    url(r'^$', views.RestaurantListView.as_view(), name='list'),
    url(r'^create$', views.RestaurantCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', views.RestaurantDetailView.as_view(), name='detail'),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.RestaurantListAPIView.as_view(), name='list'),
    url(r'^create/$', views.RestaurantCreateAPIView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', views.RestaurantRetrieveAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/update$', views.RestaurantUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete$', views.RestaurantDeleteAPIView.as_view(), name='delete'),
]

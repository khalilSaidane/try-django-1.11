from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.MenuListView.as_view(), name='list'),
    url(r'^create$', views.MenuCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.MenuDetailView.as_view(), name='detail'),
]

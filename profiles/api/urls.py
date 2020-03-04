from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<username>[\w]+)/follow/$', views.ProfileFollowAPIToggle.as_view(), name='follow-toggle'),
]


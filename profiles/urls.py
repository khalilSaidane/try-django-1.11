from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<username>[\w]+)/$', views.ProfileDetailView.as_view(), name='detail'),
]

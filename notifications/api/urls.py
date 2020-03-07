from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<pk>\d+)/update$', views.NotificationAPIView.as_view(), name='update'),
    url(r'$', views.NotificationAPIListView.as_view(), name='list'),
]


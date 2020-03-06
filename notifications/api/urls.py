from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'$', views.NotificationAPIListView.as_view(), name='list'),
]


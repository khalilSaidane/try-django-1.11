"""cfehome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from profiles.views import ProfileFollowToggle
from menus.views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^restaurants/', include('restaurents.urls', namespace='restaurants')),
    url(r'^menus/', include('menus.urls', namespace='menus')),
    url(r'^profiles/', include('profiles.urls', namespace='profiles')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^about/', TemplateView.as_view(template_name='home/about.html'), name='about'),
    url(r'^contact/', TemplateView.as_view(template_name='home/contact.html'), name='contact'),
    url(r'^home/', HomeView.as_view(), name='home'),
    url(r'^follow/', ProfileFollowToggle.as_view(), name='follow'),

]

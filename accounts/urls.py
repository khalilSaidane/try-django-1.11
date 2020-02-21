from django.conf.urls import url
from . import views


urlpatterns = [
    url('register', views.Register.as_view(), name='register'),
    url('login', views.UserLoginView.as_view(), name='login'),
    url('logout', views.LogoutView.as_view(), name='logout'),
    url('change-password', views.ChangePasswordView.as_view(), name='change_password'),
]

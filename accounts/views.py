from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView  # LogoutView and PasswordChangeForm are used in urls.py, do not delete it !
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin


class Register(SuccessMessageMixin,generic.CreateView):
    model = User
    template_name = 'accounts/register.htm'
    success_url = 'accounts/login'
    form_class = UserCreationForm
    success_message = "User %(username)s successfully created"


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    success_message = "Welcome %(username)s"


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'accounts/change-password.html'
    success_url = '/restaurants'
    success_message = "Password changed successfully"




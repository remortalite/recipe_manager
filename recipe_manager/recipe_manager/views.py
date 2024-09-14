from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


# Create your views here.
class LoginView(auth_views.LoginView):
    template_name = 'auth/login.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('home')


class LogoutView(auth_views.LogoutView):
    next_page = "/"

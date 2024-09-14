from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


# Create your views here.
class LoginView(auth_views.LoginView):
    template_name = 'auth/login.html'
    success_url = reverse_lazy('home')

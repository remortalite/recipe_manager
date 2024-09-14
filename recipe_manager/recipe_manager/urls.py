from django.urls import path
from django.views.generic import TemplateView

from .views import LoginView, LogoutView


urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='home'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
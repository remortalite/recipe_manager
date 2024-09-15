from django.urls import path

from .views import UserCreationView

urlpatterns = [
    path('create/', UserCreationView.as_view(), name='users.create'),
]

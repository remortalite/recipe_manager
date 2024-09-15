from django.shortcuts import render
from django.views.generic import CreateView

from .forms import UserCreationForm
from .models import User


class UserCreationView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'form.html'

    extra_context = {
        'title': 'Create user',
        'header': 'Create user',
        'button_text': 'Sign up',
    }

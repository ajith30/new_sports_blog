from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm #Built-in model form(User model)which is exist in django we can create our own form
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.

class signUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

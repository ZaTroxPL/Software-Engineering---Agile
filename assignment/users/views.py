from typing import Any
from django.db import models
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy

# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserChangeView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/edit_profile.html'

    def get_object(self):
        return self.request.user

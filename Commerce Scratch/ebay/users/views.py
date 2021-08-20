from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView 
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from .forms import user_register_form
# Create your views here.

class LoginView(LoginView):
    template_name ="users/login.html"


class LogoutView(LogoutView):
    pass;   

class RegisterView(CreateView):    
    model = get_user_model()
    template_name= 'users/register.html'
    form_class = user_register_form 
    success_url = '/'

    

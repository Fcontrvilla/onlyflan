from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from .forms import FomularioRegistro
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class Registro(SuccessMessageMixin, CreateView):
    form_class = FomularioRegistro
    template_name = "users/registro.html"
    success_url = reverse_lazy("login")   #solo en clases
    success_message = "Registro exitoso!!"


class Login(LoginView):
    template_name = "users/login.html"


class Logout(LogoutView):     # sin template
    next_page = reverse_lazy("home")
    http_method_names = [ "get", "post"]

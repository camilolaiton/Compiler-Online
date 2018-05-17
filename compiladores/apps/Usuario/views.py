from django.shortcuts import render, redirect
from apps.Usuario.forms import LoginForm, RegisterForm
from django.contrib.auth.views import FormView, logout
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.

class LoginView(FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = "Usuario/login.html"

    def form_valid(self, form):
        request = self.request
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("/register")
        return super(LoginView, self).form_invalid(form)

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'Usuario/registrar.html'
    success_url = '/login'

def LogOut(request):
    logout(request)
    return redirect("/login")

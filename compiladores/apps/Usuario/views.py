from django.shortcuts import render, redirect
from apps.Usuario.forms import LoginForm, RegisterForm
from django.contrib.auth.views import FormView, logout
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import authenticate, login as auth_login
from apps.Usuario.models import Usuario
from apps.PerfilUsuario.models import PerfilUsuario

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
            print("Nombre de usuario que entra: ", user.username)
            print("Email de usuario que entra: ", user.email)

            try:
                Perfil = PerfilUsuario.objects.get(usuario=user)
                print("perfiles: " , Perfil)
                return redirect('/logout')

            except PerfilUsuario.DoesNotExist:
                return redirect("/register")

        return super(LoginView, self).form_invalid(form)

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'Usuario/registrar.html'
    success_url = '/logout'

class UsuarioUpdate(UpdateView):
    model = Usuario
    fields = ['username', 'email']
    template_name = 'Usuario/actualizar.html'
    success_url = '/logout'

def LogOut(request):
    logout(request)
    return redirect("/login")

def Principal(request):
    return render(request, "Usuario/Principal.html")
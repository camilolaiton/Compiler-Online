from django.shortcuts import render, redirect
from apps.Usuario.forms import LoginForm, RegisterForm
from django.contrib.auth.views import FormView, logout
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

from apps.Usuario.models import Usuario
from apps.PerfilUsuario.models import PerfilUsuario
from apps.lenguaje.models import Lenguaje
from apps.pais.models import Pais
from apps.codigo.models import Codigo

from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import JsonResponse, HttpResponse

from apps.Usuario.parser import *

# Create your views here.

class LoginView(FormView):
    form_class = LoginForm
    success_url = '/principal'
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

            return redirect('/principal')

        messages.warning(request, 'Nombre de usuario o contraseña incorrectos')
        return super(LoginView, self).form_invalid(form)

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'Usuario/registrar.html'
    success_url = 'logout'

class UsuarioUpdate(UpdateView):
    model = PerfilUsuario
    fields = ['nombre1', 'nombre2', 'apellido1', 'apellido2', 'edad', 'ciudad', 'telefono', 'pais', 'lenguaje']
    template_name = 'Usuario/actualizar.html'
    success_url = '/principal'

def LogOut(request):
    logout(request)
    return redirect("/login")

def Principal(request):
    return render(request, "Usuario/Principal.html")

def Estadisticas(request):
    return render(request, 'Usuario/estadisticas.html')

def Eliminar(request, pk):
    try:
        usuarioEliminar = Usuario.objects.get(id=pk)
        usuarioEliminar.is_active = False
        usuarioEliminar.save()

        return LogOut(request)

    except:
        print("No se pudo eliminar el usuario, ha ocurrido algun error")

    return Principal(request)

def recibirCodigo(request):

    if request.method == 'POST':

        print(request.user.perfil)

        if(request.POST['nombreCodigo'] != ""):
            codigo_buscado = Codigo.objects.get(perfil = request.user.perfil, filename=request.POST['nombreCodigo'])
            var = int(codigo_buscado.cantidadEjecuciones)
            var += 1
            codigo_buscado.cantidadEjecuciones = var
            codigo_buscado.save()

        contenido = request.POST['contenido']

        #Trabajo con el compilador eblack
        contenido = contenido.replace("'", '')
        contenido = contenido.split('\n')

        printed_info.clear()

        for i in contenido:
            t = p.parse(i)

        enviar = ""

        for x in printed_info:
            enviar = str(enviar) + ">>" + str(x) + str('\n')

        return JsonResponse({"resultado": enviar})
    else:
        return HttpResponse("Peticion no valida")

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        lenguajes = Lenguaje.objects.all()
        paises = Pais.objects.all()

        labeles = []
        labeles_paises = []
        default_items2 = []
        default_itemsPaises = []

        for i in lenguajes:
            labeles.append(i.__str__())
            default_items2.append(PerfilUsuario.objects.filter(lenguaje=i).count())

        for x in paises:
            labeles_paises.append(x.__str__())
            default_itemsPaises.append(PerfilUsuario.objects.filter(pais=x).count())

        #print(labeles)

        users_count = Usuario.objects.all().count()
        labels = labeles #["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = default_items2

        data = {
            "UsuariosXLenguaje":{"labels":labels,"defaultData": default_items,},
            "UsuariosXPais":{"labels":labeles_paises, "defaultData":default_itemsPaises,},
        }

        return Response(data)
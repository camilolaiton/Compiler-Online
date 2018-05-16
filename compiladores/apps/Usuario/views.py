from django.shortcuts import render, redirect
from apps.Usuario.forms import UsuarioForm
# Create your views here.

def login(request):
    return render(request, 'Usuario/login.html')

def usuario_view(request):

    if request.method == 'POST':

        form = UsuarioForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('login')

    else:
        form = UsuarioForm()

    return render(request, 'Usuario/Usuario_form.html', {'form':form})
"""
def auth_view(request):
    email = request.POST.get('email','')
    password = request.POST.get('password','')
    usuario = auth.authenticate(email=email, password=password)

    if usuario is not None:
        auth.login(request, usuario)
        return render(request, 'Usuario/Usuario_form.html')#Cambiar por la pagina principal
    else:
        return render(request, 'Usuario/login.html')
"""

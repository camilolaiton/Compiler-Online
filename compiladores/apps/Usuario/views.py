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
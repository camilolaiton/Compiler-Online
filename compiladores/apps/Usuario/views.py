from django.shortcuts import render, redirect
from apps.Usuario.forms import UsuarioForm
# Create your views here.

def index(request):
    return render(request, 'Usuario/index.html')

def usuario_view(request):

    if request.method == 'POST':

        form = UsuarioForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('index')

    else:
        form = UsuarioForm()

    return render(request, 'Usuario/Usuario_form.html', {'form':form})
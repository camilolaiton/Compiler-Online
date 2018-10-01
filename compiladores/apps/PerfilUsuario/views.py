from apps.PerfilUsuario.forms import CreateForm
from django.views.generic import CreateView
from django.shortcuts import redirect, render
from apps.PerfilUsuario.forms import PerfilForm
from apps.Usuario.models import Usuario
from apps.PerfilUsuario.models import PerfilUsuario

# Create your views here.

class RegisterView(CreateView):
    form_class = CreateForm
    template_name = 'PerfilUsuario/crearPerfil.html'
    success_url = '../principal'

def crear_perfil(request):

    if request.method == 'POST':
        form = PerfilForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            print("Username: ", username)

            try:
                usuario_buscado = Usuario.objects.get(username=username)

                print("Buscando usuario")

                if usuario_buscado.perfil == None:

                    form.save()

                    try:
                        print("Buscando perfil")

                        perfil_buscado = PerfilUsuario.objects.get(username=username)
                        usuario_buscado.perfil = perfil_buscado
                        usuario_buscado.save()

                    except PerfilUsuario.DoesNotExist:
                        print("Perfil no encontrado")

            except Usuario.DoesNotExist:
                print("No se pudo crear el usuario")


        return redirect('principal')

    else:
        form = PerfilForm()

        return render(request, 'PerfilUsuario/crearPerfil.html', {'form': form})
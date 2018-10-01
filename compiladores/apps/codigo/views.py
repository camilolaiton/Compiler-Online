from django.http import JsonResponse, HttpResponse
from apps.codigo.models import Codigo
from django.shortcuts import render
from apps.PerfilUsuario.models import PerfilUsuario

"""
from django.shortcuts import render, redirect  # puedes importar render_to_response
from apps.codigo.forms import UploadForm
from apps.codigo.models import Codigo
from apps.PerfilUsuario.models import PerfilUsuario


def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Codigo(filename=request.POST['filename'], docfile=request.FILES['docfile'], cantidadEjecuciones = 0, perfil = request.user.perfil)
            newdoc.save(form)
            return redirect("../principal")
    else:
        form = UploadForm()

    # tambien se puede utilizar render_to_response
    # return render_to_response('upload.html', {'form': form}, context_instance = RequestContext(request))
    return render(request, 'Codigo/codigo.html', {'form': form})


"""

def CodigoView(request, pk):
    perfil = PerfilUsuario.objects.get(id = pk)
    codigos = Codigo.objects.filter(perfil = perfil)
    print(codigos)
    contexto = {'codigos':codigos}
    return render(request, 'Codigo/archivosUsuario.html', contexto)

def upload_file(request):

    if request.method == 'POST':

        if request.user.perfil == None:
            return JsonResponse({"resultado": str(request.user) + ", actualice su perfil primero.", "mensaje": 0})
        else:
            try:
                buscar_codigo = Codigo.objects.get(filename=request.POST['filename'])
                buscar_codigo.docfile = request.POST['contenido']
                buscar_codigo.save()

                print("Codigo existente")

                return JsonResponse({"resultado": str(request.user) + ", su archivo ya ha sido actualizado", "mensaje": 0})

            except Codigo.DoesNotExist:

                nuevoCodigo = Codigo(filename=request.POST['filename'], docfile=request.POST['contenido'], cantidadEjecuciones=0, perfil=request.user.perfil)
                nuevoCodigo.save()

        return JsonResponse({"resultado": "Codigo subido con exito!", "mensaje": 1})
    else:
        return HttpResponse("Peticion no valida")

def get_file(request):

    if request.method == 'POST':

        if request.user.perfil == None:
            return JsonResponse({"resultado": str(request.user) + ", actualice su perfil primero.", "mensaje": 0})
        else:
            try:
                buscar_codigo = Codigo.objects.get(filename=request.POST['filename'], perfil=request.user.perfil)
                #print(buscar_codigo.docfile)

                return JsonResponse({"resultado": buscar_codigo.docfile, "mensaje": 1})

            except Codigo.DoesNotExist:

                return JsonResponse({"resultado": "El archivo no ha sido encontrado!", "mensaje": 0})

    else:
        return HttpResponse("Peticion no valida")
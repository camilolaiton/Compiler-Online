from apps.Usuario.models import Usuario
from apps.PerfilUsuario.models import PerfilUsuario
from django.shortcuts import redirect

def create_profile(strategy, details, response, user, *args, **kwargs):

    print("details: ", details)
   # print("args: ", args)
   # print("kwargs: ", kwargs)
    #print("response: ", response)

    print("details - username: ", details['username'])
    print("details - email: ", details['email'])
    print("details - fullname: ", details['fullname'])
    print("details - first_name: ", details['first_name'])
    print("details - last_name: ", details['last_name'])

    print(user)

    try:
        perfil_buscado = PerfilUsuario.objects.get(usuario=user)
        print("Se ha encontrado el perfil")

    except PerfilUsuario.DoesNotExist:
        print("No se ha encontrado el perfil")
        print("detail: ", details['username'])

        try:
            email = details['email']
            print(email)
            usuario_buscado = Usuario.objects.get(email=email)
            print("paso 1")
            nuevoPerfil = PerfilUsuario(nombre1=details['first_name'], apellido1=details['last_name'],
                                        usuario=user)
            nuevoPerfil.save()

        except Usuario.DoesNotExist:

            new_profile = Usuario(username=details['username'], email=details['email'])
            new_profile.save()
            
            nuevoPerfil = PerfilUsuario(nombre1=details['first_name'], apellido1=details['last_name'],
                                        usuario=user)
            nuevoPerfil.save()

    return kwargs
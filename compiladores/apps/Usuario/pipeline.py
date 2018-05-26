from apps.Usuario.models import Usuario
<<<<<<< HEAD
from apps.PerfilUsuario.models import PerfilUsuario
=======
>>>>>>> 2c134556564fbfb5e50c9cc71f2d3503aae54c65
from django.shortcuts import redirect

def create_profile(strategy, details, response, user, *args, **kwargs):

    print("details: ", details)
<<<<<<< HEAD
   # print("args: ", args)
   # print("kwargs: ", kwargs)
    #print("response: ", response)
=======
    print("args: ", args)
    print("kwargs: ", kwargs)
    print("response: ", response)
>>>>>>> 2c134556564fbfb5e50c9cc71f2d3503aae54c65

    print("details - username: ", details['username'])
    print("details - email: ", details['email'])
    print("details - fullname: ", details['fullname'])
    print("details - first_name: ", details['first_name'])
    print("details - last_name: ", details['last_name'])

<<<<<<< HEAD
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
=======
    if Usuario.objects.filter(username=user).exists():
        pass
    else:
        new_profile = Usuario(username=user)
        new_profile.save()
>>>>>>> 2c134556564fbfb5e50c9cc71f2d3503aae54c65

    return kwargs
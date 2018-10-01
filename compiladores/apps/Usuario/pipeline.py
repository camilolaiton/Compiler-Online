from apps.Usuario.models import Usuario
from apps.PerfilUsuario.models import PerfilUsuario

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

    print("username2: ", user.username)

    try:
        usuario_buscado = Usuario.objects.get(username=details['username'])
        print("Se ha encontrado el usuario")

        try:
            perfil_buscado = PerfilUsuario.objects.get(username=details['username'])
            print("Se ha encontrado el perfil")

        except PerfilUsuario.DoesNotExist:

            nuevoPerfil = PerfilUsuario(username=details['username'], nombre1=details['first_name'],
                                        apellido1=details['last_name'])
            nuevoPerfil.save()

            usuario_buscado.perfil = nuevoPerfil
            usuario_buscado.save()

    except Usuario.DoesNotExist:
        print("No se ha encontrado el usuario")
        print("detail: ", details['username'])

        nuevoPerfil = PerfilUsuario(username=details['username'], nombre1=details['first_name'], apellido1=details['last_name'])
        nuevoPerfil.save()

        new_profile = Usuario(username=details['username'], email=details['email'], perfil=nuevoPerfil)
        new_profile.save()

    return kwargs
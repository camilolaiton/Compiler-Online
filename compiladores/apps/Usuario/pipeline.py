from apps.Usuario.models import Usuario
from django.shortcuts import redirect

def create_profile(strategy, details, response, user, *args, **kwargs):

    print("details: ", details)
    print("args: ", args)
    print("kwargs: ", kwargs)
    print("response: ", response)

    print("details - username: ", details['username'])
    print("details - email: ", details['email'])
    print("details - fullname: ", details['fullname'])
    print("details - first_name: ", details['first_name'])
    print("details - last_name: ", details['last_name'])

    if Usuario.objects.filter(username=user).exists():
        pass
    else:
        new_profile = Usuario(username=user)
        new_profile.save()

    return kwargs
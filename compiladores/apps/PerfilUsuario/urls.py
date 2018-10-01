from apps.PerfilUsuario.views import RegisterView, crear_perfil
from django.urls import path

urlpatterns = [
    path('crearPerfil', crear_perfil, name='crearPerfil'),
]
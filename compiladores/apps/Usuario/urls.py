from apps.Usuario.views import usuario_view, index
from django.urls import path

urlpatterns = [
    path('new', usuario_view, name = 'Usuario_crear'),
    path('', index, name='index'),
]
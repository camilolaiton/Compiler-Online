from apps.Usuario.views import usuario_view, login
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('new', usuario_view, name = 'usuario_nuevo'),
    path('login', login, name='login'),
]
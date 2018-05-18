from apps.Usuario.views import LoginView, RegisterView, LogOut, UsuarioUpdate, Principal
from django.urls import path


urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='registrar'),
    path('logout', LogOut, name='logout'),
    path('actualizar/<int:pk>/', UsuarioUpdate.as_view(), name='actualizar'),
    path('principal', Principal, name="principal"),
]
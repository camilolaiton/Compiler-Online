from apps.Usuario.views import LoginView, RegisterView, LogOut, UsuarioUpdate, Principal, Eliminar, Estadisticas, ChartData, recibirCodigo
from django.urls import path


urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('registrar', RegisterView.as_view(), name='registrar'),
    path('logout', LogOut, name='logout'),
    path('actualizar/<int:pk>/', UsuarioUpdate.as_view(), name='actualizar'),
    path('principal', Principal, name="principal"),
    path('eliminar/<int:pk>/', Eliminar, name='eliminar'),
    path('Chart/data/', ChartData.as_view(), name='ChartData'),
    path('estadisticas', Estadisticas, name='estadisticas'),
    path('enviarCodigo/', recibirCodigo, name='recibirCodigo'),
]
from django.urls import path
from apps.codigo.views import upload_file, CodigoView, get_file

urlpatterns = [
    path('subirCodigo/', upload_file, name='subirCodigo'),
    path('buscarCodigo/', get_file, name='buscarCodigo'),
    path('codigos/<int:pk>/', CodigoView, name='codigos'),
]
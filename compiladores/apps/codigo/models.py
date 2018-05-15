from django.db import models
from apps.Usuario.models import Usuario
# Create your models here.

class Codigo(models.Model):

    codigo = models.TextField()
    cantidadEjecuciones = models.PositiveSmallIntegerField()
    idUsuario = models.OneToOneField(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    FechaCreacion = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.codigo
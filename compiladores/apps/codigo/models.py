from django.db import models
from apps.PerfilUsuario.models import PerfilUsuario
# Create your models here.

class Codigo(models.Model):

    filename = models.CharField(max_length=35)
    docfile =  models.CharField(max_length=100)
    cantidadEjecuciones = models.IntegerField(default=0)
    perfil = models.ForeignKey(PerfilUsuario, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.filename
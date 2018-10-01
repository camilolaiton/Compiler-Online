from django.db import models
from apps.pais.models import Pais
from apps.lenguaje.models import Lenguaje

# Create your models here.

class PerfilUsuario(models.Model):

    username = models.CharField(max_length=35)
    nombre1 = models.CharField(max_length=35)
    nombre2 = models.CharField(max_length=35)
    apellido1 = models.CharField(max_length=35)
    apellido2 = models.CharField(max_length=35)
    edad = models.CharField(max_length=4)
    ciudad = models.CharField(max_length=35)
    telefono = models.CharField(max_length=35)
    pais = models.ForeignKey(Pais, null=True, blank=True, on_delete=models.CASCADE)
    lenguaje = models.ForeignKey(Lenguaje, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.username.__str__()

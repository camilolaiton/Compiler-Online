from django.db import models
from apps.pais.models import Pais
from apps.lenguaje.models import Lenguaje

# Create your models here.

class PerfilUsuario(models.Model):

    nombre1 = models.CharField(max_length=35)
    nombre2 = models.CharField(max_length=35)
    apellido1 = models.CharField(max_length=35)
    apellido2 = models.CharField(max_length=35)
    edad = models.CharField(max_length=4)
    ciudad = models.CharField(max_length=35)
    telefono = models.CharField(max_length=35)
    pais = models.ForeignKey(Pais, null=True, blank=False, on_delete=models.CASCADE)
    lenguaje = models.ForeignKey(Lenguaje, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        cadena = self.nombre1 + " " + self.nombre2 + " " + self.apellido1 + " " + self.apellido2
        return cadena

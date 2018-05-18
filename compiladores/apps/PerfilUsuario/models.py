from django.db import models
from apps.pais.models import Pais
from apps.lenguaje.models import Lenguaje
from apps.Usuario.models import Usuario

# Create your models here.

class PerfilUsuario(models.Model):

    nombre1 = models.CharField(max_length=35)
    nombre2 = models.CharField(max_length=35)
    apellido1 = models.CharField(max_length=35)
    apellido2 = models.CharField(max_length=35)
    edad = models.CharField(max_length=4)
    ciudad = models.CharField(max_length=35)
    telefono = models.CharField(max_length=35)
    pais = models.ForeignKey(Pais, null=True, blank=True, on_delete=models.CASCADE)
    lenguaje = models.ForeignKey(Lenguaje, null=True, blank=True, on_delete=models.CASCADE)
    usuario = models.OneToOneField(Usuario, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.__str__()

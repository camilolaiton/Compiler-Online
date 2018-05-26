from django.db import models
from apps.pais.models import Pais
from apps.lenguaje.models import Lenguaje
<<<<<<< HEAD
from apps.Usuario.models import Usuario
=======
>>>>>>> 2c134556564fbfb5e50c9cc71f2d3503aae54c65

# Create your models here.

class PerfilUsuario(models.Model):

    nombre1 = models.CharField(max_length=35)
    nombre2 = models.CharField(max_length=35)
    apellido1 = models.CharField(max_length=35)
    apellido2 = models.CharField(max_length=35)
    edad = models.CharField(max_length=4)
    ciudad = models.CharField(max_length=35)
    telefono = models.CharField(max_length=35)
<<<<<<< HEAD
    pais = models.ForeignKey(Pais, null=True, blank=True, on_delete=models.CASCADE)
    lenguaje = models.ForeignKey(Lenguaje, null=True, blank=True, on_delete=models.CASCADE)
    usuario = models.OneToOneField(Usuario, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.__str__()
=======
    pais = models.ForeignKey(Pais, null=True, blank=False, on_delete=models.CASCADE)
    lenguaje = models.ForeignKey(Lenguaje, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        cadena = self.nombre1 + " " + self.nombre2 + " " + self.apellido1 + " " + self.apellido2
        return cadena
>>>>>>> 2c134556564fbfb5e50c9cc71f2d3503aae54c65

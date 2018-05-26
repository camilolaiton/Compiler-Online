from django.db import models

# Create your models here.

class Pais(models.Model):

    pais = models.CharField(max_length=35)

    def __str__(self):
        return self.pais


class Lenguaje(models.Model):

    lenguaje = models.CharField(max_length=35)

    def __str__(self):
        return self.lenguaje


class Usuario(models.Model):

    nombre1 = models.CharField(max_length=35)
    nombre2 = models.CharField(max_length=35)
    apellido1 = models.CharField(max_length=35)
    apellido2 = models.CharField(max_length=35)
    edad = models.CharField(max_length=4)
    ciudad = models.CharField(max_length=35)
    email = models.EmailField(max_length=35)
    telefono = models.CharField(max_length=35)
    idpais = models.ForeignKey(Pais, null=False, blank=False, on_delete=models.CASCADE)
    idlenguaje = models.ForeignKey(Lenguaje, null=False, blank=False, on_delete=models.CASCADE)


    def nombreCompleto(self):
        nombreCompleto = "{0} {1} {2} {3}"
        return nombreCompleto.format(self.nombre1, self.nombre2, self.apellido1, self.apellido2)


    def __str__(self):
        return self.nombreCompleto()


class Codigo(models.Model):

    codigo = models.TextField()
    cantidadEjecuciones = models.PositiveSmallIntegerField()
    idUsuario = models.OneToOneField(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    FechaCreacion = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.codigo

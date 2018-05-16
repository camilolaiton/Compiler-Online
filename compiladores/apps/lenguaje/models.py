from django.db import models

# Create your models here.

class Lenguaje(models.Model):

    lenguaje = models.CharField(max_length=35, unique=True)

    def __str__(self):
        return self.lenguaje
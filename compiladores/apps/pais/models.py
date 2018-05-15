from django.db import models

# Create your models here.

class Pais(models.Model):

    pais = models.CharField(max_length=35)

    def __str__(self):
        return self.pais
from django.contrib import admin
from apps.GestionUsuarios.models import *

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Pais)
admin.site.register(Lenguaje)
admin.site.register(Codigo)
from django.contrib import admin
from apps.Usuario.models import Usuario

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']
    class Meta:
        model = Usuario

admin.site.register(Usuario, UserAdmin)

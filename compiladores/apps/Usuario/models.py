from django.db import models
from apps.pais.models import Pais
from apps.lenguaje.models import Lenguaje
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, nombre1, nombre2, apellido1, apellido2, edad, ciudad, telefono, pais, lenguaje, password=None, is_active=True , is_staff=False, is_admin=False):
        if not email:
            raise ValueError('Los usuarios deben tener una direccion de correo')
        if not password:
            raise ValueError('Los usuarios deben tener una password')
        if not nombre1:
            raise ValueError('Los usuarios deben tener un primer nombre')
        if not nombre2:
            raise ValueError('Los usuarios deben tener un segundo nombre')
        if not apellido1:
            raise ValueError('Los usuarios deben tener un primer apellido')
        if not apellido2:
            raise ValueError('Los usuarios deben tener un segundo apellido')
        if not edad:
            raise ValueError('Los usuarios deben tener una edad')
        if not ciudad:
            raise ValueError('Los usuarios deben tener una ciudad')
        if not telefono:
            raise ValueError('Los usuarios deben tener un telefono')

        usuario_obj = self.model(
            email=self.normalize_email(email),
            nombre1=nombre1,
            nombre2=nombre2,
            apellido1=apellido1,
            apellido2=apellido2,
            edad=edad,
            ciudad=ciudad,
            telefono=telefono,
            pais=pais,
            lenguaje=lenguaje
        )

        usuario_obj.set_password(password)#Change user password
        usuario_obj.staff = is_staff
        usuario_obj.admin = is_admin
        usuario_obj.active = is_active
        usuario_obj.save(using=self._db)
        return usuario_obj

    def create_staffuser(self, email, nombre1, nombre2, apellido1, apellido2, edad, ciudad, telefono, pais, lenguaje, password=None):
        usuario = self.create_user(
            email,
            nombre1,
            nombre2,
            apellido1,
            apellido2,
            edad,
            ciudad,
            telefono,
            pais,
            lenguaje,
            password=password,
            is_staff=True
        )
        return usuario

    def create_superuser(self, email, nombre1, nombre2, apellido1, apellido2, edad, ciudad, telefono, password=None):

        usuario = self.create_user(
            email,
            nombre1,
            nombre2,
            apellido1,
            apellido2,
            edad,
            ciudad,
            telefono,
            pais=None,
            lenguaje=None,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return usuario

class Usuario(AbstractBaseUser):

    nombre1 = models.CharField(max_length=35)
    nombre2 = models.CharField(max_length=35)
    apellido1 = models.CharField(max_length=35)
    apellido2 = models.CharField(max_length=35)
    edad = models.CharField(max_length=4)
    ciudad = models.CharField(max_length=35)
    telefono = models.CharField(max_length=35)
    pais = models.ForeignKey(Pais, null=True, blank=False, on_delete=models.CASCADE)
    lenguaje = models.ForeignKey(Lenguaje, null=True, blank=False, on_delete=models.CASCADE)

    email = models.EmailField(max_length=50, unique=True)
    active = models.BooleanField(default=True) #can login
    staff = models.BooleanField(default=False) #staff user non superuser
    admin = models.BooleanField(default=False) #Superuser

    USERNAME_FIELD = 'email'#username
    #Email and password are required by default
    REQUIRED_FIELDS = ['nombre1', 'nombre2', 'apellido1', 'apellido2', 'edad', 'ciudad', 'telefono']

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

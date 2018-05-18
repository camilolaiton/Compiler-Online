from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, is_active=True , is_staff=False, is_admin=False):

        if not username:
            raise ValueError('Los usuarios deben tener una cuenta de usuario')
        #if not email:
         #   raise ValueError('Los usuarios deben tener una direccion de correo')

        """nombre1, nombre2, apellido1, apellido2, edad, ciudad, telefono, pais, lenguaje,"""

        """
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
            
        nombre1=nombre1,
        nombre2=nombre2,
        apellido1=apellido1,
        apellido2=apellido2,
        edad=edad,
        ciudad=ciudad,
        telefono=telefono,
        pais=pais,
        lenguaje=lenguaje
            
        

        """

        usuario_obj = self.model(
            username=username,
            email=self.normalize_email(email)
        )

        usuario_obj.set_password(password)#Change user password
        usuario_obj.staff = is_staff
        usuario_obj.admin = is_admin
        usuario_obj.active = is_active
        usuario_obj.save(using=self._db)
        return usuario_obj

    def create_staffuser(self, username, email, password=None):
        usuario = self.create_user(
            username,
            email,
            password=password,
            is_staff=True
        )
        return usuario

    def create_superuser(self, username, email, password=None):

        usuario = self.create_user(
            username,
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return usuario

class Usuario(AbstractBaseUser):

    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(max_length=50)
    active = models.BooleanField(default=True) #can login
    staff = models.BooleanField(default=False) #staff user non superuser
    admin = models.BooleanField(default=False) #Superuser

    USERNAME_FIELD = 'username'#username
    #Email and password are required by default
    REQUIRED_FIELDS = [ 'email']

    objects = UserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

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

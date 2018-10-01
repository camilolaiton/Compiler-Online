from django.db import models
from apps.PerfilUsuario.models import PerfilUsuario

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email, perfil=None, password=None, active=True, staff=False, admin=False):

        if not username:
            raise ValueError('Los usuarios deben tener una cuenta de usuario')

        usuario_obj = self.model(
            username=username,
            email=self.normalize_email(email),
            perfil=perfil
        )

        usuario_obj.set_password(password)#Change user password
        usuario_obj.is_staff = staff
        usuario_obj.is_admin = admin
        usuario_obj.is_active = active
        usuario_obj.save(using=self._db)
        return usuario_obj

    def create_staffuser(self, username, email, password=None):
        usuario = self.create_user(
            username,
            email,
            password=password,
            staff=True
        )
        return usuario

    def create_superuser(self, username, email, password=None):

        usuario = self.create_user(
            username,
            email,
            password=password,
            staff=True,
            admin=True
        )
        return usuario

class Usuario(AbstractBaseUser):

    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(max_length=50)
    perfil = models.OneToOneField(PerfilUsuario, null=True, blank=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False) #can login
    is_staff = models.BooleanField(default=False) #staff user non superuser
    is_admin = models.BooleanField(default=False) #Superuser

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
    def staff(self):
        return self.is_staff

    @property
    def admin(self):
        return self.is_admin

    @property
    def active(self):
        return self.is_active

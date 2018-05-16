from django import forms
from apps.Usuario.models import Usuario
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario

        fields = [
            'nombre1',
            'nombre2',
            'apellido1',
            'apellido2',
            'edad',
            'ciudad',
            'email',
            'password',
            'telefono',
            'pais',
            'lenguaje',
        ]

        labels = {
            'nombre1': 'Primer Nombre',
            'nombre2': 'Segundo Nombre',
            'apellido1': 'Primer Apelido',
            'apellido2': 'Segundo Apellido',
            'edad': 'Edad',
            'ciudad': 'Ciudad',
            'email': 'Email',
            'password': 'Contraseña',
            'telefono': 'Telefono',
            'pais':'Pais',
            'lenguaje':'Lenguaje',
        }

        widgets = {
            'nombre1': forms.TextInput(attrs={'class':'form-control'}),
            'nombre2': forms.TextInput(attrs={'class':'form-control'}),
            'apellido1': forms.TextInput(attrs={'class':'form-control'}),
            'apellido2': forms.TextInput(attrs={'class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'ciudad': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.Select(attrs={'class': 'form-control'}),
            'lenguaje': forms.Select(attrs={'class': 'form-control'}),
        }

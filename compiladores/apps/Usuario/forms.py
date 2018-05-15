from django import forms
from apps.Usuario.models import Usuario

class GestionUsuariosForm(forms.ModelForm):

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
            'contraseña',
            'telefono',
            'idpais',
            'idlenguaje',
        ]

        labels = {
            'nombre1': 'Primer Nombre',
            'nombre2': 'Segundo Nombre',
            'apellido1': 'Primer Apelido',
            'apellido2': 'Segundo Apellido',
            'edad': 'Edad',
            'ciudad': 'Ciudad',
            'email': 'Email',
            'contraseña': 'Contraseña',
            'telefono': 'Telefono',
            'idpais': 'Pais',
            'idlenguaje': 'Lenguaje',
        }

        widgets = {
            'nombre1': forms.TextInput(attrs={'class':'form-control'}),
            'nombre2': forms.TextInput(attrs={'class':'form-control'}),
            'apellido1': forms.TextInput(attrs={'class':'form-control'}),
            'apellido2': forms.TextInput(attrs={'class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'ciudad': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'contraseña': forms.PasswordInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'idpais': forms.Select(attrs={'class':'form-control'}),
            'idlenguaje': forms.Select(attrs={'class':'form-control'}),
        }
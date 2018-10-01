from django import forms
from apps.PerfilUsuario.models import PerfilUsuario

class PerfilForm(forms.ModelForm):

    class Meta:
        model = PerfilUsuario

        fields = [
            'username',
            'nombre1',
            'nombre2',
            'apellido1',
            'apellido2',
            'edad',
            'ciudad',
            'telefono',
            'pais',
            'lenguaje',
        ]

        labels = {
            'username':'Nombre de usuario',
            'nombre1': 'Primer Nombre',
            'nombre2': 'Segundo Nombre',
            'apellido1': 'Primer Apelido',
            'apellido2': 'Segundo Apellido',
            'edad': 'Edad',
            'ciudad': 'Ciudad',
            'telefono': 'Telefono',
            'pais':'Pais',
            'lenguaje':'Lenguaje',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'nombre1': forms.TextInput(attrs={'class':'form-control'}),
            'nombre2': forms.TextInput(attrs={'class':'form-control'}),
            'apellido1': forms.TextInput(attrs={'class':'form-control'}),
            'apellido2': forms.TextInput(attrs={'class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'ciudad': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'pais': forms.Select(attrs={'class': 'form-control'}),
            'lenguaje': forms.Select(attrs={'class': 'form-control'}),
        }


class CreateForm(forms.ModelForm):

    #'nombre1', 'nombre2', 'apellido1', 'apellido2', 'edad', 'ciudad', 'telefono','pais', 'lenguaje',

    class Meta:
        model = PerfilUsuario
        fields = ( 'nombre1','nombre2', 'apellido1', 'apellido2', 'edad', 'ciudad', 'telefono','pais', 'lenguaje')


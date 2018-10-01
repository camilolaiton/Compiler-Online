from django import forms
from apps.codigo.models import Codigo

class UploadForm(forms.ModelForm):

    class Meta:
        model = Codigo

        fields = [
            'filename',
            'docfile',
            'cantidadEjecuciones',
            'perfil',
        ]

        labels = {
            'filename':'Nombre de archivo',
            'docfile': 'Seleccione el archivo',
            'cantidadEjecuciones': 'cantidad de ejecuciones',
            'perfil': 'Usuario',
        }

        widgets = {
            'filename': forms.TextInput(attrs={'class':'form-control'}),
            'docfile': form.TextInput(attrs={'class':'form-control'}),
            'cantidadEjecuciones': forms.TextInput(attrs={'class':'form-control'}),
            'perfil': forms.TextInput(attrs={'class':'form-control'}),
        }

"""
class UploadForm(forms.Form):
    filename = forms.CharField(max_length=100)
    docfile = forms.FileField(
        label='Selecciona un archivo'
    )
    cantidadEjecuciones = forms.IntegerField()
    perfil = forms.Select()

"""
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
            'pais': forms.Select(attrs={'class': 'form-control'}),
            'lenguaje': forms.Select(attrs={'class': 'form-control'}),
        }

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('nombre1', 'nombre2', 'apellido1', 'apellido2', 'edad', 'ciudad', 'telefono','email', 'pais', 'lenguaje',)

    def clean_password(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.active = True

        if commit:
            user.save()
        return user

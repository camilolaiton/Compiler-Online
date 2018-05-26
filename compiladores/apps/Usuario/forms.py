from django import forms
from apps.Usuario.models import Usuario
<<<<<<< HEAD
=======
from django.contrib.auth.forms import ReadOnlyPasswordHashField
>>>>>>> 2c134556564fbfb5e50c9cc71f2d3503aae54c65

class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    #'nombre1', 'nombre2', 'apellido1', 'apellido2', 'edad', 'ciudad', 'telefono','pais', 'lenguaje',

    class Meta:
        model = Usuario
        fields = ( 'username','email',)

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

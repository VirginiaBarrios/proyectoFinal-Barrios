from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm (UserCreationForm):
    email=forms.EmailField(label="Email usuario")
    password1=forms.EmailField(label="Contraseña ", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contraseña ", widget=forms.PasswordInput)
    first_name=forms.CharField(label="Nombre usuario")
    last_name=forms.CharField(label="Apellido usuario")
    bio=forms.CharField(label="Biografía")

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2", "bio"]
        help_texts= {k:"" for k in fields}
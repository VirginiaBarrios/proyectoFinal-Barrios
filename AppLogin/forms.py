from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class RegistroUsuarioForm (UserCreationForm):
    email=forms.EmailField(label="Email usuario")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contraseña ", widget=forms.PasswordInput)
    first_name=forms.CharField(label="Nombre", max_length=50)
    last_name=forms.CharField(label="Apellido", max_length=50)
    bio=forms.CharField(label="Biografía", widget=forms.Textarea)

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2", "first_name", "last_name", "bio"]
        help_texts= {k:"" for k in fields}
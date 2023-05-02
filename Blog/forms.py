from .models import Posteos, SobreMi, Contacto
from AppLogin import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponse





class RegistroUsuarioForm (UserCreationForm):
    email=forms.EmailField(label="Email usuario")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contraseña ", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts= {k:"" for k in fields}

class SobreMiForm (forms.Form):
    titulo=forms.CharField(max_length=200)
    subtitulo=forms.CharField(max_length=200)
    #texto=forms.TextField()
    def __str__(self):
        return f"{self.titulo} - {self.subtitulo}"


class PosteoForm (forms.Form):
    titulo=forms.CharField(max_length=200)
    subtitulo=forms.CharField(max_length=200)
    autor=forms.CharField(max_length=50)
    fecha=forms.DateField()
    #texto=forms.TextField()
    imagen=forms.ImageField()
    def __str__(self):
        return f"{self.titulo} - {self.subtitulo}"

class ContactoForm (forms.Form):
    nombre=forms.CharField(max_length=50)
    #email=forms.EmailField(max_length=254, default='default@example.com')
    numero=forms.IntegerField()
    #mensaje=forms.TextField()
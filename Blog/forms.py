from .models import Posteos, SobreMi
from AppLogin import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User


class SobreMiForm (forms.Form):
    titulo=forms.CharField(max_length=200)
    subtitulo=forms.CharField(max_length=200)
    mensaje = forms.CharField(widget=forms.Textarea)


class PosteoForm (forms.Form):
    titulo=forms.CharField(max_length=200)
    subtitulo=forms.CharField(max_length=200)
    autor=forms.CharField(max_length=50)
    fecha=forms.DateField()
    mensaje = forms.CharField(widget=forms.Textarea)




class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=50, initial='')
    email = forms.EmailField()
    numero = forms.IntegerField()
    mensaje = forms.CharField(widget=forms.Textarea)



class RegistroUsuarioForm (UserCreationForm):
    cddemail=forms.EmailField(label="Email usuario")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contraseña ", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts= {k:"" for k in fields}

    
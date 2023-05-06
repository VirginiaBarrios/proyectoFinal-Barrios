from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

#AppPerfiles
class UserEditForm(UserCreationForm):
    email=forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    first_name= forms.CharField(label="Modificiar nombre")
    last_name= forms.CharField(label="Modificar apellido")
    class Meta:
        model=User
        fields=["email","password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen = forms.ImageField(label="Imagen")


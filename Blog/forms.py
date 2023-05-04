from .models import Posteos, SobreMi
from AppLogin import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget

class SobreMiForm (forms.Form):
    titulo=forms.CharField(max_length=200)
    subtitulo=forms.CharField(max_length=200)
    mensaje = forms.CharField(widget=forms.Textarea)


class PosteoForm(forms.Form):
    titulo = forms.CharField(max_length=200)
    subtitulo = forms.CharField(max_length=200)
    autor = forms.CharField(max_length=50)
    fecha = forms.DateField()
    texto = forms.CharField(widget=CKEditorWidget())





class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=50, initial='')
    email = forms.EmailField()
    numero = forms.IntegerField()
    mensaje = forms.CharField(widget=forms.Textarea)



class RegistroUsuarioForm (UserCreationForm):
    email=forms.EmailField(label="Email usuario")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contraseña ", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts= {k:"" for k in fields}



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



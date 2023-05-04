from .models import Posteos, SobreMi, Contacto
from django import forms
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











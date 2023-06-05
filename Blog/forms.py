from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Posteos

class SobreMiForm (forms.Form):
    titulo=forms.CharField(max_length=200)
    subtitulo=forms.CharField(max_length=200)
    mensaje = forms.CharField(widget=forms.Textarea)


class PosteoForm(forms.ModelForm):
    class Meta:
        model = Posteos
        fields = ['titulo', 'subtitulo', 'autor', 'fecha', 'texto']
        widgets = {'texto': CKEditorWidget()}



class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=50, initial='')
    email = forms.EmailField()
    numero = forms.IntegerField()
    mensaje = forms.CharField(widget=forms.Textarea)

class EditarPostForm(forms.Form):
    titulo = forms.CharField(max_length=200)
    subtitulo = forms.CharField(max_length=200)
    autor = forms.CharField(max_length=50)
    fecha = forms.DateField()
    texto = forms.CharField(widget=CKEditorWidget())













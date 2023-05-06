from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.


class SobreMi(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    texto = models.TextField(default='')

class Posteos(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=50)
    fecha = models.DateField()
    texto = RichTextField()
    
    def _str_(self):
        return f"{self.titulo} - {self.subtitulo} - {self.autor} - {self.fecha} - {self.texto}"

class Contacto(models.Model):
    nombre = models.CharField(max_length=50, default='')
    email = models.EmailField(default='example@example.com')
    numero = models.IntegerField(default= 1111111)
    mensaje = models.TextField(default='')

    def _str_(self):
        return f"{self.nombre} - {self.email} - {self.numero} - {self.mensaje}"




from django.db import models

# Create your models here.


class SobreMi (models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    texto = models.TextField()

class Posteos (models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=50)
    fecha = models.DateField()
    texto = models.TextField()
    def __str__(self):
        return f"{self.titulo} - {self.subtitulo} - {self.autor} - {self.fecha} - {self.texto}"

class Contacto (models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    numero = models.IntegerField()
    mensaje = models.TextField()
    def __str__(self):
        return f"{self.nombre} - {self.email} - {self.numero} - {self.mensaje}"



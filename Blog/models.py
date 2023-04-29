from django.db import models

# Create your models here.



class SobreMi (models.Model):
    titulo=models.CharField(max_length=200)
    subtitulo=models.CharField(max_length=200)
    texto=models.TextField()
    def __str__(self):
        return f"{self.titulo} - {self.subtitulo}"


class Posteos (models.Model):
    titulo=models.CharField(max_length=200)
    subtitulo=models.CharField(max_length=200)
    autor=models.CharField(max_length=50)
    fecha=models.TimeField()
    texto=models.TextField()



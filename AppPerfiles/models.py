from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MiPerfil(models.Model):
    avatar = models.ImageField(width_field=100, height_field=100)
    nombre = models.CharField(max_length=50, default='')
    apellido = models.CharField(max_length=50, default='')
    email = models.EmailField(default='example@example.com')
    def __str__(self):
        return f"{self.avatar} {self.nombre} {self.apellido} - {self.email}"


class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
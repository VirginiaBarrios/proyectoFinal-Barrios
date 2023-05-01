from django.urls import path
from .views import * 

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('contacto/', contacto, name="Contacto"),
    path('posteos/', posteos, name="Posteos"),
    path('sobreMi/', sobreMi, name="SobreMi"),
    path('imagenInicio/', imagenInicio, name="ImagenInicio"),
    path('iniciarSesion/', iniciarSesion, name= "IniciarSesion"),
    path('registro/', registro, name= "Registro"),
    path('crearPosteo/', crearPosteo, name="crearPosteo"),
]
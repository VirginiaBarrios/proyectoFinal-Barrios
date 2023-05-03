from django.urls import path
from .views import * 
from AppLogin import urls
from AppRegistro import urls
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('contacto/', contacto, name="Contacto"),
    path('posteos/', posteos, name="Posteos"),
    path('sobreMi/', sobreMi, name="SobreMi"),
    path('crearPosteo/', crearPosteo, name="CrearPosteo"),
    path('registro/', registro, name= "Registro"),
     path('iniciarSesion/', iniciarSesion, name= "IniciarSesion"),
    path('finalizarSesion/', LogoutView.as_view(template_name='finalizarSesion.html'), name='FinalizarSesion')

    
    
]
from django.urls import path, include
from .views import * 


urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('contacto/', contacto, name="Contacto"),
    path('posteos/', posteos, name="Posteos"),
    path('sobreMi/', sobreMi, name="SobreMi"),
    
    path('AppLogin/', include ('AppLogin.urls')),
    path('AppRegistro/', include ('AppRegistro.urls')),
    path('AppPerfiles/', include ('AppPerfiles.urls')),
    
    path('ckeditor/', include ('ckeditor_uploader.urls')),
    
    path('vistaPost/<int:id>', vistaPost, name="vistaPost"),
    path('buscarPost/', buscarPost, name="buscarPost"),
    path('busquedaPosts/', busquedaPosts, name="busquedaPosts"),
    path('editarPost/<titulo>', editarPost, name="editarPost"),
    path('eliminarPost/<id>', eliminarPost, name="eliminarPost"),
]
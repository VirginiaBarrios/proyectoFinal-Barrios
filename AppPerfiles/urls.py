from django.urls import path
from .views import * 

urlpatterns = [
 path('editarPerfil/', editarPerfil, name= "editarPerfil"),


]
from django.urls import path
from .views import * 
from django.contrib.auth.views import LogoutView




urlpatterns = [

 path('registro/', registro, name= "Registro"),
 


]
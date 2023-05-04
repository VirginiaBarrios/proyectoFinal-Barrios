from django.urls import path
from .views import * 
from django.contrib.auth.views import LogoutView




urlpatterns = [
 path('iniciarSesion/', iniciarSesion, name= "IniciarSesion"),
 path('finalizarSesion/', LogoutView.as_view(template_name='finalizarSesion.html'), name='FinalizarSesion')


]
from django.urls import path
from .views import * 

urlpatterns = [
    path('Blog/', inicio, name="inicio"),
    path('Blog/', contacto, name="contacto"),
    path('Blog/', posteos, name="posteos"),
    path('Blog/', sobreMi, name="sobreMi"),
    
]
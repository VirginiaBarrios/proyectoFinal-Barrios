from django.urls import path
from .views import * 

urlpatterns = [
    path('Blog1/', inicio, name="inicio"),
    path('Blog2/', contacto, name="contacto"),
    path('Blog3/', posteos, name="posteos"),
    path('Blog4/', sobreMi, name="SobreMi"),
    
]
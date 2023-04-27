from django.urls import path
from .views import *

urlpatterns = [
    path('inicio/', inicio_app, name="inicio"),
]
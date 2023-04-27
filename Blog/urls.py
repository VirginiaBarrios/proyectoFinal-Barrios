from django.urls import path
from .views import * 

urlpatterns = [
    path('Blog/', inicio, name="inicio"),
]
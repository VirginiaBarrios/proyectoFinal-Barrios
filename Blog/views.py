from django.shortcuts import render

# Create your views here.

def inicio(request): 
    return render(request, "inicio.html")

def contacto(request):
    return render(request, "contact.html")

def posteos(request):
    return render(request, "post.html")

def sobreMi(request):
    return render(request, "about.html")




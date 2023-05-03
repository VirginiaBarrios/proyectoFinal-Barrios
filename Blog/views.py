from django.shortcuts import render
from .models import Posteos, SobreMi
from .forms import SobreMiForm, PosteoForm, ContactoForm, RegistroUsuarioForm
from django.conf import settings
from AppLogin import views
from AppRegistro import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail


# Create your views here.

def inicio(request): 
    return render(request, "inicio.html")


def contacto(request):
   
    return render(request, "contact.html")


@login_required
def posteos(request):
    return render(request, "post.html")

def sobreMi(request):
    return render(request, "about.html")

@login_required
def crearPosteo(request):
    if request.method == "POST":
        form = PosteosForm(request.POST)
        if form.is_valid():
            posteo = Posteo()
            posteo.titulo = form.cleaned_data['titulo']
            posteo.subtitulo = form.cleaned_data['subtitulo']
            posteo.autor = form.cleaned_data['autor']
            posteo.fecha = form.cleaned_data['autor']
            posteo.texto = form.cleaned_data['texto']
            posteo.save()
            form = PosteoForm()
    else:
        form = PosteoForm
    posteos = Posteos.objects.all()
    context = {"posteos": posteos, "form": form}
    return render(request, "crearPosteo.html", context)

def iniciarSesion(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "inicio.html", {"mensaje":f"Usuario {usu} logueado correctamente"})
            else:
                return render(request, "iniciarSesion.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "iniciarSesion.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request,"iniciarSesion.html", {"form":form})


def registro(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
            return render(request, "inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "registro.html", {"form": form, "mensaje": "Error al crear el usuario"})
    else:
        form=RegistroUsuarioForm()
        return render(request, "registro.html", {"form": form})
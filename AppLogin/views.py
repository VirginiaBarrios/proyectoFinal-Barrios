from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm 
from Blog.views import obtenerAvatar


#login logout register

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
                return render(request, "inicio.html", {"mensaje":f"Usuario {usu} logueado correctamente", "avatar": obtenerAvatar(request)})
            else:
                return render(request, "iniciarSesion.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos", "avatar": obtenerAvatar(request)})
        else:
            return render(request, "iniciarSesion.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos", "avatar": obtenerAvatar(request)})
    else:
        form=AuthenticationForm()
        return render(request,"iniciarSesion.html", {"form":form, "avatar": obtenerAvatar(request)})



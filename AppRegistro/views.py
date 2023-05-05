from django.shortcuts import render
from .forms import RegistroUsuarioForm
from Blog.views import obtenerAvatar
# Create your views here.

def registro(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
            return render(request, "inicio.html", {"mensaje":f"Usuario {username} creado correctamente", "avatar": obtenerAvatar(request)})
        else:
            return render(request, "registro.html", {"form": form, "mensaje": "Error al crear el usuario" ,"avatar": obtenerAvatar(request)})
    else:
        form=RegistroUsuarioForm()
        return render(request, "registro.html", {"form": form, "avatar": obtenerAvatar(request)})
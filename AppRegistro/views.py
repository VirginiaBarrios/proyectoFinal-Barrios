from django.shortcuts import render
from .forms import RegistroUsuarioForm
# Create your views here.

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
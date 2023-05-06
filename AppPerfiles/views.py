from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm, AvatarForm
from Blog.views import obtenerAvatar
from .models import MiPerfil, Avatar
# Create your views here.


#AppPerfiles


@login_required

def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.bio=info["bio"]
            usuario.save()
            return render(request, "inicio.html", {"mensaje":f"Usuario {usuario.username} editado correctamente.", "avatar": obtenerAvatar(request)})
        else:
            return render(request, "editarPerfil.html", {"form": form, "nombreusuario": usuario.username, "avatar": obtenerAvatar(request)})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "editarPerfil.html", {"form": form, "nombreusuario": usuario.username, "avatar": obtenerAvatar(request)})


def miPerfil(request):
    miPerfil = MiPerfil.objects.first()  # obtiene el primer perfil
    return render(request, 'miPerfil.html', {'miPerfil': miPerfil, "avatar": obtenerAvatar(request)})
            


@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar = Avatar.objects.filter(user=request.user)
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar = Avatar(user=request.user, imagen=form.cleaned_data['imagen'])
            avatar.save()
            return render(request, "inicio.html", {"mensaje": f"Avatar agregado correctamente", "avatar": obtenerAvatar(request)})
        else:
            return render(request, "agregarAvatar.html", {"form": form, "usuario": request.user, "mensaje": "Error al agregar nuevo avatar", "avatar": obtenerAvatar(request)})
    else:
        form = AvatarForm()








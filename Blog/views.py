from django.shortcuts import render
from .models import Posteos, SobreMi, Contacto, Avatar
from .forms import SobreMiForm, PosteoForm, ContactoForm, AvatarForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail



# Create your views here.

def inicio(request): 
    return render(request, "inicio.html", {"avatar": obtenerAvatar(request)})


def contacto(request):
    if request.method=="POST":
        subject=request.POST["asunto"]
        message=request.POST["mensaje"] + " " + request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["emaildeprueba765@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)
    return render(request, "contact.html", {"avatar": obtenerAvatar(request)})


def sobreMi(request):
    return render(request, "about.html", {"avatar": obtenerAvatar(request)})


#Posts
@login_required
def posteos(request):
    if request.method == "POST":
        form = PosteoForm(request.POST)
        if form.is_valid():
            posteo = Posteos()
            posteo.titulo = form.cleaned_data['titulo']
            posteo.subtitulo = form.cleaned_data['subtitulo']
            posteo.autor = form.cleaned_data['autor']
            posteo.fecha = form.cleaned_data['fecha']
            posteo.texto = form.cleaned_data['texto']
            posteo.save()
            form = PosteoForm()
    else:
        form = PosteoForm()
    posteos = Posteos.objects.all()
    context = {"posteos": posteos, "form": form, "avatar": obtenerAvatar(request)}
    return render(request, "post.html", context)

@login_required

def vistaPost(request, posteo_id):
    posteo = Posteos.objects.get(id=posteo_id)
    context = {'posteo': posteo, "avatar": obtenerAvatar(request)}
    return render(request, 'vistaPost.html', context)


@login_required
def mostrarPosteos(request):
    posteos = Posteos.objects.all()
    context = {'posteos': posteos, "avatar": obtenerAvatar(request)}
    return render(request, 'mostrarPosteos.html', context)



 
#Imagenes de avatares
@login_required
def obtenerAvatar(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if len(avatares) != 0:
        return avatares[0].imagen.url
    else:
        return "/media/avatares/default.png"


@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar = Avatar.objects.filter(user=request.user)
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "incio.html", {"mensaje": f"Avatar agregado correctamente"})
        else:
            return render(request, "agregarAvatar.html", {"form": form, "usuario": request.user, "mensaje": "Error al agregar nuevo avatar"})
    else:
        form = AvatarForm()
        return render(request, "agregarAvatar.html", {"form": form, "usuario": request.user, "avatar": obtenerAvatar(request)})
                





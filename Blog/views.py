from django.shortcuts import render
from .models import Posteos, SobreMi, Contacto, Avatar
from .forms import SobreMiForm, PosteoForm, ContactoForm
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



@login_required
def posteos(request):
    if request.method == "POST":
        form = Posteos(request.POST)
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
        form = PosteoForm
    posteos = Posteos.objects.all()
    context = {"posteos": posteos, "form": form, "avatar": obtenerAvatar(request)}
    return render(request, "post.html", context)




 
#Imagenes de avatares

def obtenerAvatar(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if len(avatares) != 0:
        return avatares[0].imagen.url
    else:
        return "/media/avatares/default.png"




def vistaPost(request):
    vistaPost = Posteos.objects.first()  # obtiene el primer perfil
    return render(request, 'vistaPost.html', {'vistaPost': vistaPost, "avatar": obtenerAvatar(request)})
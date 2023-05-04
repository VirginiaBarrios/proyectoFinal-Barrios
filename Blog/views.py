from django.shortcuts import render
from .models import Posteos, SobreMi, Contacto, Avatar
from .forms import SobreMiForm, PosteoForm, ContactoForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail






# Create your views here.

def inicio(request): 
    return render(request, "inicio.html")


def contacto(request):
    if request.method=="POST":
        subject=request.POST["asunto"]
        message=request.POST["mensaje"] + " " + request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["emaildeprueba765@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)
   
    return render(request, "contact.html")


@login_required
def posteos(request):
    return render(request, "post.html")

def sobreMi(request):
    return render(request, "about.html")





@login_required
def crearPosteo(request):
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
        form = PosteoForm
    posteos = Posteos.objects.all()
    context = {"posteos": posteos, "form": form}
    return render(request, "crearPosteo.html", context)




 
#Imagenes de avatares


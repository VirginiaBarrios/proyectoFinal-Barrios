from django.shortcuts import render
from .models import Posteos
from .forms import PosteoForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from AppPerfiles.models import Avatar
from proyectoFinal import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.


def inicio(request):
    posteos = Posteos.objects.all()
    paginator = Paginator(posteos, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posteos': posteos,'page_obj': page_obj, "avatar": obtenerAvatar(request)}
    return render(request, 'inicio.html', context)



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
def vistaPost(request, id):
    posteo = Posteos.objects.get(id=id)
    context = {'posteo': posteo, "avatar": obtenerAvatar(request)}
    if request.user.is_authenticated:
        return render(request, 'vistaPost.html', context)
    else:
        return render(request, 'inicio.html', context, {"mensaje":"Inicia sesion para ver el contenido"} )


def buscarPost(request):
    return render(request, "busquedaPosts.html", {"posteos": posteos, "avatar": obtenerAvatar(request)})

def busquedaPosts(request):
    autorIngresado = request.GET['autor']
    if autorIngresado!="":
        posteos = Posteos.objects.filter(autor__icontains=autorIngresado)
        print(posteos)
        return render(request, "resultadosBusquedaPosts.html", {"posteos": posteos, "avatar": obtenerAvatar(request)})
    else:
        return render(request, "busquedaPosts.html", {"mensaje": "Por favor ingrese un autor", "avatar": obtenerAvatar(request)})



@login_required
def editarPost(request, id):
    posteos = get_object_or_404(Posteos, id=id)
    if request.method == 'POST':
        form = PosteoForm(request.POST, instance=posteos)
        if form.is_valid(): 
            form.save()
            return redirect('Inicio')
    else:
        form = PosteoForm(instance=posteos)
    return render(request, 'editarPost.html', {'form': form})



def eliminarPost(request, id):
    posteos=Posteos.objects.get(id=id)
    print(posteos)
    posteos.delete()
    posteos=Posteos.objects.all()
    return render(request, "post.html", {"posteos": posteos, "mensaje":"Post eliminado correctamente"})
 

#Imagenes de avatares
@login_required
def obtenerAvatar(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if len(avatares) != 0:
        return avatares[0].imagen.url
    else:
        return "/media/avatares/default.png"




from django.shortcuts import render
from ArtistZoneApp.forms import PublicacionesForm
from .models import Publicaciones
from django import http
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(request):
    return render(request,'ArtistZoneApp/index.html')

def publicaciones(request):

    publicaciones = Publicaciones.objects.all()
    datos = {
        "listaPublicaciones":publicaciones
    }
    return render(request, 'ArtistZoneApp/publicaciones.html',datos)

def publicar(request):
    datos = {
        'form':PublicacionesForm()
    }
    if request.method == "POST":
        formulario = PublicacionesForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return http.HttpResponseRedirect("http://127.0.0.1:8000/publicar/")
            datos['mensaje'] = "Gurdado correctamente"
        datos['form'] = formulario
    return render(request, 'ArtistZoneApp/publicar.html',datos)

def galery(request):
    return render(request,'ArtistZoneApp/galery.html')

def picture(request):
    return render(request,'ArtistZoneApp/picture.html')

def search(request):
    return render(request,'ArtistZoneApp/galery.html')

def register(request):

    return render(request,'ArtistZoneApp/register.html')

def login(request):
    return render(request,'ArtistZoneApp/login.html')


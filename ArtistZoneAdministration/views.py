from django import forms
from ArtistZoneAdministration.forms import PersonasForm
from django.shortcuts import redirect, render
from .models import Personas
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def administrar(request):
    personas = Personas.objects.all()
    context ={
        'personas':personas
    }
    return render(request, 'ArtistZoneAdministration/administrar.html',context)

def crearPersona(request):
    if request.method == 'GET':
        form = PersonasForm()
        context = {
            'form':form
        }
    else:
        form =PersonasForm(request.POST)
        context = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('Administrar')
        
    return render(request, 'ArtistZoneAdministration/crear_persona.html',context)

def editarPersona(request, id):
    persona = Personas.objects.get(id = id)
    if request.method=='GET':
        form = PersonasForm(instance = persona)
        context ={
            'form':form
        }
    else:
        form= PersonasForm(request.POST, instance= persona)
        context ={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('Administrar')
    return render(request, 'ArtistZoneAdministration/crear_persona.html',context)

def eliminarPersona(request, id):
    persona = Personas.objects.get(id=id)
    persona.delete()
    return redirect('Administrar')
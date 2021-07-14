from ArtistZoneApp.forms import PublicacionesForm
from django import forms
from django.contrib.auth.views import LoginView
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from ArtistZoneAdministration.forms import PersonasForm
from django.shortcuts import redirect, render
from .models import Personas
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from ArtistZoneApp.models import Publicaciones
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'ArtistZoneAdministration/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('Administrar')


@login_required(login_url="http://127.0.0.1:8000/login/")
def administrar(request):
    publicaciones = Publicaciones.objects.all()
    datos = {
        "listaPublicaciones":publicaciones
    }
    
    return render(request, 'ArtistZoneAdministration/administrar.html',datos)

@login_required(login_url="http://127.0.0.1:8000/login/")
def crearPublicaion(request):
    if request.method == 'GET':
        form = PublicacionesForm()
        context = {
            'form':form
        }
    else:
        form =PublicacionesForm(request.POST)
        context = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('Administrar')
        
    return render(request, 'ArtistZoneAdministration/gestion_publicaciones.html',context)

@login_required(login_url="http://127.0.0.1:8000/login/")
def editarPublicacion(request, id):
    publicacion = Publicaciones.objects.get(id = id)
    if request.method=='GET':
        form = PublicacionesForm(instance = publicacion)
        context ={
            'form':form
        }
    else:
        form= PublicacionesForm(request.POST, instance= publicacion)
        context ={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('Administrar')
    return render(request, 'ArtistZoneAdministration/gestion_publicaciones.html',context)

@login_required(login_url="http://127.0.0.1:8000/login/")
def eliminarPublicacion(request, id):
    publicacion = Publicaciones.objects.get(id=id)
    publicacion.delete()
    return redirect('Administrar')



class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('Administrar')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('Administrar')
        return super(RegisterPage, self).get(*args, **kwargs)
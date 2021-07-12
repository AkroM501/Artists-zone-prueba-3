from core.forms import VehiculoForm
from django.shortcuts import render
from .models import Vehiculo

class Ninja:
    def __init__(self,nombre,aldea):
        self.nombre = nombre
        self.aldea = aldea
        super().__init__()  
# Create your views here.
def home(request):
    vehiculos = Vehiculo.objects.all()
    datos = {
        "listaVehiculos":vehiculos
    }
    return render(request,'core/home.html',datos)

def listanaruto(request):
    personaje1 = Ninja("Naruto","Hoja")

    listaPJ = ["Oroshimaru","Jiraiya","Tsunade"]

    contexto = {"nombre":"Shikamaru","lista":listaPJ,"personaje1":personaje1}

    return render(request,'core/listanaruto.html',contexto)

def form_vehiculo(request):
    datos = {
        'form':VehiculoForm()
    }
    if request.method == "POST":
        formulario = VehiculoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Gurdado correctamente"
    return render(request,'core/form_vehiculo.html',datos)

def form_mod_vehiculo(request,id):
    vehiculo = Vehiculo.objects


# -------------------------------------------------------------
def index(request):
    return render(request,'core/index.html')

def galery(request):
    return render(request,'core/galery.html')

def picture(request):
    return render(request,'core/picture.html')

def search(request):
    return render(request,'core/galery.html')

def register(request):
    return render(request,'core/register.html')

def login(request):
    return render(request,'core/login.html')




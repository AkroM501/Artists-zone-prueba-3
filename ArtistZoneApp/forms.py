from django import forms
from django.forms import ModelForm, fields
from .models import Publicaciones, Usuarios

class PublicacionesForm(ModelForm):
    class Meta:
        model = Publicaciones
        fields= ['nombre_cuadro','nombre_autor','precio','imagen_cuadro']

class RegistroForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombre_usuario']
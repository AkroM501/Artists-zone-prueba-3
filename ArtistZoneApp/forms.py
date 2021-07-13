from django import forms
from django.forms import ModelForm
from .models import Publicaciones

class PublicacionesForm(ModelForm):
    class Meta:
        model = Publicaciones
        fields= ['nombre_cuadro','nombre_autor','precio','imagen_cuadro']
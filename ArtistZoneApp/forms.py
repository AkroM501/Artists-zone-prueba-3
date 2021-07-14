from django import forms
from django.forms import ModelForm, fields
from .models import Publicaciones


class PublicacionesForm(ModelForm):
    class Meta:
        model = Publicaciones
        fields= '__all__'


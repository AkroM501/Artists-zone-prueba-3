from django import forms
from django.forms import fields
from .models import Personas
from ArtistZoneApp.models import Publicaciones

class PersonasForm(forms.ModelForm):
    class Meta:
        model = Personas
        fields='__all__'

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicaciones
        fields='__all__'
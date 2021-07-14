from django import forms
from django.forms import fields
from .models import Personas

class PersonasForm(forms.ModelForm):
    class Meta:
        model = Personas
        fields='__all__'
from django.db import models
from django import forms
from django.forms.widgets import Widget

class Publicaciones(models.Model):
    nombre_cuadro = models.CharField(max_length=30)
    nombre_autor = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagen_cuadro = models.ImageField(upload_to="cuadros",null=True)

    def __str__(self):
        return self.nombre_cuadro

class Usuarios(models.Model):
    nombre_usuario=models.CharField(max_length=30)
    contrasenna =models.CharField(max_length=30)
    email=models.EmailField(blank=True,null=True)

    def __str__(self):
        return self.nombre_usuario
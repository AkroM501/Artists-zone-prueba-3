from django.db import models


class Publicaciones(models.Model):
    nombreCuadro = models.CharField(max_length=30)
    nombreAutor = models.CharField(max_length=50)
    precio = models.IntegerField()
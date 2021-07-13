from django.db import models

class Publicaciones(models.Model):
    nombre_cuadro = models.CharField(max_length=30)
    nombre_autor = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagen_cuadro = models.ImageField(upload_to="cuadros",null=True)

    def __str__(self):
        return self.nombre_cuadro
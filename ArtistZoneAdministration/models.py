from django.db import models

# Create your models here.
class Personas(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)

    def __str__(self):
        return self.nombre

# class Task=(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     title = models.CharField(max_length=200, null=True, blank=True)
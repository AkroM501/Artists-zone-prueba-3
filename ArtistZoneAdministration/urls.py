from django.contrib import admin
from django.urls import path, include
from ArtistZoneAdministration import views


import ArtistZoneAdministration


urlpatterns = [
    path('administrar/',views.administrar,name="Administrar"),
    path('gestion/',views.crearPersona,name="Gestion"),
    path('editar/<int:id>/',views.editarPersona,name="Editar"),
    path('eliminar/<int:id>/',views.eliminarPersona,name="Eliminar"),

]
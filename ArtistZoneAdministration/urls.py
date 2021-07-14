from django.contrib import admin
from django.urls import path, include
from ArtistZoneAdministration import views
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('administrar/',views.administrar,name="Administrar"),
    path('gestion/',views.crearPublicaion,name="Gestion"),
    path('editar/<int:id>/',views.editarPublicacion,name="Editar"),
    path('eliminar/<int:id>/',views.eliminarPublicacion,name="Eliminar"),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

]
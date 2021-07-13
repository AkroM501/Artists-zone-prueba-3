from django.urls import path
from ArtistZoneApp import views

urlpatterns = [
    path('',views.home,name="Home"),
    path('galery/',views.galery,name="Galery"),
    path('galery/picture.html',views.picture,name="Picture"),
    path('picture.html/',views.picture,name="Picture"),
    path('galery/galery.html',views.search,name="Picture"),
    path('galery.html',views.search,name="Search"),
    path('register/',views.register,name="Register"),
    # path('login/',views.login,name="Login"),
    path('publicaciones/',views.publicaciones,name="Publicaciones"),
    path('publicar/',views.publicar,name="Publicar"),
]
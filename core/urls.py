from django.urls import path
from .views import home, listanaruto, form_vehiculo, index, galery, picture, search, register, login


urlpatterns = [
    path('',home,name="home"),
    path('listanaruto/',listanaruto,name="listanaruto"),
    path('form-vehiculo',form_vehiculo,name="form_vehiculo"),
    path('index/',index,name="index"),
    path('galery/',galery,name="galery"),
    path('galery/picture.html',picture,name="picture"),
    path('index/picture.html',picture,name="picture"),
    path('galery/galery.html',search,name="picture"),
    path('index/galery.html',search,name="search"),
    path('register/',register,name="register"),
    path('login/',login,name="login")


]
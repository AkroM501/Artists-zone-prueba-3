from django.shortcuts import render


def home(request):
    return render(request,'ArtistZoneApp/index.html')

def galery(request):
    return render(request,'ArtistZoneApp/galery.html')

def picture(request):
    return render(request,'ArtistZoneApp/picture.html')

def search(request):
    return render(request,'ArtistZoneApp/galery.html')

def register(request):
    return render(request,'ArtistZoneApp/register.html')

def login(request):
    return render(request,'ArtistZoneApp/login.html')
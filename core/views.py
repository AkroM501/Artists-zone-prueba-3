from django.shortcuts import render

def home(request):
    return render(request,'core/index.html')

def galery(request):
    return render(request,'core/galery.html')

def picture(request):
    return render(request,'core/picture.html')

def search(request):
    return render(request,'core/galery.html')

def register(request):
    return render(request,'core/register.html')

def login(request):
    return render(request,'core/login.html')




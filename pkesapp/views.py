from django.shortcuts import render
from .models import Servicios


def home(request):
    return render(request, 'home.html')

def tienda(request):
    return render(request, 'tienda.html')

def blog(request):
    return render(request, 'blog.html')    

def about(request):
    return render(request, 'about.html')    

def services(request):
    servicios = Servicios.objects.all()
    return render(request, 'services.html', {'servicios':servicios})  


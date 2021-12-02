from django.shortcuts import render
from .models import Galeria

def galeria(request):
    galerias = Galeria.objects.all()
    data = {
        'galerias': galerias
    } 
    return render(request, 'galeria.html', data)    

def otono(request):
    return render(request, 'gal_otono.html')

def casual(request):
    return render(request, 'gal_casual.html') 
    
def elegante(request):
    return render(request, 'gal_elegante.html')

def infantil(request):
    return render(request, 'gal_infantil.html')   
    
def personalizados(request):
    return render(request, 'gal_personalizados.html')

def masculino(request):
    return render(request, 'gal_masculino.html')
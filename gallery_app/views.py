from django.shortcuts import render
from .models import Gallery

def gallery(request):
    galleries = Gallery.objects.all()
    data = {
        'galleries': galleries
    } 
    return render(request, 'gallery.html', data)   

def autumn(request):
    return render(request, 'gal_autumn.html')   

def casual(request):
    return render(request, 'gal_casual.html')
    
def elegant(request):
    return render(request, 'gal_elegant.html')

def kids(request):
    return render(request, 'gal_kids.html')  
    
def personalized(request):
    return render(request, 'gal_personalized.html')

def ken(request):
    return render(request, 'gal_ken.html')
from django.shortcuts import render

from .models import Services


def home(request):
    return render(request, 'home.html')


def blog(request):
    return render(request, 'blog.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    services = Services.objects.all()
    return render(request, 'services.html', {'services': services})

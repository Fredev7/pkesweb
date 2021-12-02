from django.urls import path

from . import views

urlpatterns = [
    path('', views.galeria, name='Galeria'),
    path('otono', views.otono, name='Otono'),
    path('casual', views.casual, name='Casual'),
    path('elegante', views.elegante, name='Elegante'),
    path('infantil', views.infantil, name='Infantil'),
    path('personalizados', views.personalizados, name='Personalizados'),
    path('masculino', views.masculino, name='Masculino'),
]

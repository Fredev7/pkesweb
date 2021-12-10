from django.urls import path

from . import views

urlpatterns = [
    path('', views.gallery, name='Gallery'),
    path('Autumn', views.autumn, name='Autumn'),
    path('casual', views.casual, name='Casual'),
    path('elegant', views.elegant, name='Elegant'),
    path('kids', views.kids, name='Kids'),
    path('personalized', views.personalized, name='Personalized'),
    path('ken', views.ken, name='Ken'),
]

from django.urls import path

from pkesapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('store', views.store, name='store'),
    path('blog', views.blog, name='Blog'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),   
]

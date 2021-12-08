from django.urls import path

from . import views 

app_name='store1'

urlpatterns = [
    path('', views.store, name='store'), 
    path('item/<slug:slug>', views.product_detail, name='product_detail'),
    path('search/<slug:categorySlug>', views.category_list, name='category_list'),
]



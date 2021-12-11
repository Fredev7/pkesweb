from django.urls import path

from . import views

app_name = 'store1'

urlpatterns = [
    path('', views.store, name='store'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('shop/<slug:categorySlug>', views.category_list, name='category_list'),
]

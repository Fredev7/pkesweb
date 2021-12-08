from django.shortcuts import get_object_or_404, render

from .models import Category, Product

def categories(request):   
    return {
        'categories' : Category.objects.all()
    }
    
    # render (request, {'categories':categories})

def store(request):
    products = Product.objects.all()
    return render(request, 'store.html', {'products':products})
    
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)   
    return render(request, 'detail.html', {'product': product})     

def category_list(request, categorySlug):
    category = get_object_or_404(Category, slug=categorySlug)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'products': products})

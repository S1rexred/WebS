from django.shortcuts import render
from products.models import Products

def index(request):
    context = {
        'title': 'Космос Coffee',
        'is_promotion': True,
    }
    return render(request, 'original2.html')

def product(request):
    context = {
        'products': Products.objects.all(),
         
    }
    return render(request, 'menu2.html')

from django.shortcuts import render
from product.models import Product,Phone



def index(request):
    return render(request, 'index.html')

def menu(request):
    #context = {
        #'title': 'Каталог',
        #'product': Product.object.all(),
    #}
    return render(request, 'menu2.html')

def phone(request):
    return render(request, 'forma.html')

def than(request,*args,**kwargs):
    if 'name' in request.POST:
        name = request.POST.GET['name']
        phonea = request.GET['phone']
        message = request.GET['message']
        element=Phone
        element = Phone(name=name,phone=phonea,message=message,)
        element.save(*args, **kwargs)
    return render(request, 'forma2.html') #{'name': name,
                                       #'phones' : phone})
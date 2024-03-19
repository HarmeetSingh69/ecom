from django.shortcuts import render
from .models import *

def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'home.html', context)

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

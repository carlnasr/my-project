from django.shortcuts import get_object_or_404 , render
from . models import Product
from datetime import datetime
# Create your views here.
def products(request):

  
    
    context = {
        'Products':Product.objects.all()
       
         
    }
    return render(request , 'products/products.html' ,context)
def product(request , pro_id):
    context = {
        'pro':get_object_or_404(Product, pk=pro_id)
    }
    return render(request , 'products/product.html', context)
def search(request):
    return render(request , 'products/search.html')
        
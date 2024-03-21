from django.shortcuts import render
from .models import product
from django.core.paginator import Paginator

# Create your views here.

def index(request):
      Featured_Products = product.objects.order_by('-priority')[:4]
      latest_Products = product.objects.order_by('-id')[:4]
      context ={
            'Featured_Products' : Featured_Products,
            'latest_Products' : latest_Products
      }
      
      return render(request,'home.html',context)

def produts(request):
      page = 1
      if request.GET:
            page=request.GET.get('page',1)
      product_list=product.objects.order_by('-priority')
      product_paginator = Paginator(product_list,3)
      product_list = product_paginator.get_page(page)
      context = {'product' : product_list}
      return render(request,'product.html',context)

def product_details(request,pk):
      products=product.objects.get(pk=pk)
      context ={'product':products}

      return render(request,'product_details.html',context)

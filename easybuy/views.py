from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import *

from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,"index.html")
def collections(request):
    category=Category.objects.filter(status=0)
    context={'category':category}
    return render(request,'product.html',context) 

def collectionsview(request,slug):
    if(Category.objects.filter(slug=slug,status=0)):
        products=Product.objects.filter(category__slug=slug)
        category=Category.objects.filter(slug=slug).first()
        context={'products':products,'category':category}
        return render(request,'display.html',context)
    else:
        messages.warning(request,"No such category found")
        return redirect('collections')

#view products
def productview(request,cate_slug,prod_slug):
    if(Category.objects.filter(slug=cate_slug,status=0)):
        if(Product.objects.filter(slug=prod_slug,status=0)):
            products=Product.objects.filter(slug=prod_slug,status=0).first()
            context={'products':products}
        else:
          messages.error(request,"No such product found")
          return redirect('collections')  


    else:
          messages.error(request,"No such category found")
          return redirect('collections') 
    return render(request,'pro_view.html',context)

def productListAjax(request):
    products=Product.objects.filter(status=0).values_list('name',flat=True)
    productsList=list(products)
    
    return JsonResponse(productsList,safe=False)

def searchproduct(request):
    if request.method == 'POST':
        searchedterm=request.POST.get('productsearch')
        if searchedterm == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            product=Product.objects.filter(name__contains=searchedterm).first()
            
            if product:
                return redirect('product/'+product.category.slug+'/'+product.slug)
            else:
                messages.info(request,"No product matched your search")
                return redirect(request.META.get('HTTP_REFERER'))
                
    return redirect(request.META.get('HTTP_REFERER'))
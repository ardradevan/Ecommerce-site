from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from easybuy.models import Cart,Order,OrderItem,Product
from django.contrib.auth.decorators import login_required
from .validation import *

@login_required(login_url='loginpage')
def index(request):
    rawcart=Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            Cart.objects.delete(id=item.id)
    cartitems=Cart.objects.filter(user=request.user)
    total_price=0
    for item in cartitems:
        total_price=total_price+item.product.selling_price * item.product_qty
    context ={'cartitems':cartitems,'total_price':total_price}        
    return render(request,"checkout.html",context)

def placeorder(request):
    if request.method =='POST':
        neworder= Order()
        neworder.user=request.user
        neworder.fname=request.POST.get('fname')
        neworder.lname=request.POST.get('lname')
        neworder.phone=request.POST.get('phone')
        neworder.email=request.POST.get('email')
        
        cart=Cart.objects.filter(user=request.user)
        cart_total_price=0
        for item in cart:
            cart_total_price=cart_total_price+item.product.selling_price*item.product_qty
            
        neworder.total_price=cart_total_price
        neworder.save()
        
        neworderitems=Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order=neworder,
                product=item.product,
                price=item.product.selling_price,
                quantity=item.product_qty
                
            )
            
        # to decrease th product quantity from available stock
        orderproduct = Product.objects.get(id=item.product_id)
        orderproduct.quantity = orderproduct.quantity - item.product_qty
        orderproduct.save()

    # to clear user's cart
    cart.delete()

    messages.success(request, "Your order placed successfully")    
    
    
    return redirect('/')    
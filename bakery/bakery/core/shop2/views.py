from decimal import Decimal
from unicodedata import category

import send_mail
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect

from .models import Product,Category


# Create your views here.


def home(request):
    products = Product.objects.all()
    categories=Category.objects.prefetch_related('products')



    if request.method == 'POST':
        email = request.POST.get('email')

        send_mail(
            subject='Welcome to Bakery',
            message=f'New user:{email}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['google@gmail.com'],
            fail_silently=False,
        )

    ctx = {'products': products}



    return render(request, 'index.html',ctx)
def error(request):
    return render(request, '404.html')
def about(request):
    return render(request, 'about.html')
def cart(request):
    return render(request, 'cart.html')
def checkout(request):
    return render(request, 'checkout.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')
def shopfull(request):
    return render(request, 'shop-fullwidth.html')
def product(request):
    return render(request, 'single-product.html')
def wishlist(request):
    return render(request, 'wishlist.html')

def add_to_cart(request,product_id):
    product = get_object_or_404(Product,id=product_id)
    cart = request.session.get('cart',{})
    pid=str(product.id)

    if pid in cart:
        cart[pid]['quantity']+=1
    else:
        cart[pid]={
            'quantity': 1,
            "price": str(product.price),
            'title': product.title,
            'image': product.image.url if product.image else '',
        }
    request.session['cart']=cart
    request.session.modified = True
    return redirect(request.META.get('HTTP_REFERER','home'))


def remove_from_cart(request,product_id):
    cart = request.session.get('cart',{})
    pid=str(product_id)

    if pid in cart:
        del cart[pid]

    request.session['cart']=cart
    request.session.modified = True

    return redirect(request.META.get('HTTP_REFERER','home'))

def cart_view(request):
    cart = request.session.get('cart',{})
    items=[]
    total=Decimal(0.00)

    for pid,item in cart.items():
        qty=item['quantity']
        price=Decimal(item['price'])
        subtotal=price*qty
        total += subtotal

        item.append({
            'product_id':pid,
            'title':item['title'],
            'image':item['image'],
            'quantity':qty,
            'price':price,
            'subtotal':subtotal,
        })

    return render(request,'cart.html',{'items':items,'total':total})






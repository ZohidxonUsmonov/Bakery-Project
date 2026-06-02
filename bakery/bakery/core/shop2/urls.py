from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('error/', error, name='error'),
    path('about/', about, name='about'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('shopfull/', shopfull, name='shopfull'),
    path('product/', product, name='product'),
    path('wishlist/', wishlist, name='wishlist'),


]

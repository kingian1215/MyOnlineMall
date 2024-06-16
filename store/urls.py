from django.contrib import admin
from django.urls import path, include
from .views import product_list, about, add_to_cart, view_cart, checkout,order_success,register
from django.contrib.auth import views as auth_views
from django.urls import path
from reservations.views import make_reservation



urlpatterns = [
    # path('', include('ecommerce_website.urls')),
    path('', product_list, name='product_list'),
    path('about/', about, name='about'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('view_cart/', view_cart, name='view_cart'),
    path('checkout/', checkout, name='checkout'),
    path('order_success/', order_success, name='order_success'),
    path('register/', register, name='register'),
    path('reservation/',make_reservation, name='make_reservation')
]

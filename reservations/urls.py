from django.urls import path
from . import views
from .views import reservation_success
from accounts.views import register
from store.views import product_list

urlpatterns = [
    # path('', views.make_reservation, name='make_reservation'),
    path('success/', reservation_success, name='reservation_success'),
    path('reservation_success/<int:email_sent>/',reservation_success, name='reservation_success'),
    path('accounts/', register, name='accounts'),
    # path('', product_list, name='product_list'),
]
from django.urls import path
from cart.views import *

urlpatterns = [
    path('cart_details/', cart_details, name='cart_details'),
    path('add_product/<int:product_id>/', add_product, name='add_product'),
    path('remove_product/<int:product_id>/', remove_product, name='remove_product'),
    path('make_order/', make_order, name='order'),
]
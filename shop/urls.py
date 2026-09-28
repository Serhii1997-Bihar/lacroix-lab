from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('categories/<int:category_id>/', categories, name='categories'),
    path('brands/<int:brand_id>/', brands, name='brands'),
    path('product_detail/<int:product_id>/', product_detail, name='product_details'),
    path('team/', team, name='team'),
]

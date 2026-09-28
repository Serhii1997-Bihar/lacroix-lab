from django.contrib import admin
from .models import Product, Size, Brand, Category, Country, Employee

class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'category', 'country', 'brand', 'image', 'video', 'price', 'about']
    search_fields = ['name']
    list_display = ['name', 'category', 'country']
admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
admin.site.register(Category, CategoryAdmin)

class CountryAdmin(admin.ModelAdmin):
    fields = ['name']
admin.site.register(Country, CountryAdmin)

class BrandAdmin(admin.ModelAdmin):
    fields = ['name']
admin.site.register(Brand, BrandAdmin)

class SizeAdmin(admin.ModelAdmin):
    fields = ['size']
admin.site.register(Size, SizeAdmin)

class AdminPanel(admin.ModelAdmin):
    fields = ['name', 'achievement', 'experience', 'image', 'bio']
    search_fields = ['name']
admin.site.register(Employee, AdminPanel)

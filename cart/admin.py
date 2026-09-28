from django.contrib import admin
from cart.models import OrderModel, ClientData

class OrderItemInline(admin.TabularInline):
    model = OrderModel
    readonly_fields = ['order', 'product', 'quantity', 'size']
    extra = 0

class OrderModelAdmin(admin.ModelAdmin):
    readonly_fields = ['name', 'address', 'phone', 'email', 'total_price', 'created_at', 'comment']
    inlines = [OrderItemInline]

admin.site.register(ClientData, OrderModelAdmin)

from django.contrib import admin
from mainapp.models import BaseUser, Order, Product



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    fields = ('name', 'desc', ('quantity', 'price'), 'image', 'product_datetime')
    search_fields = ('name',)
    readonly_fields = ('product_datetime', 'price')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('total_price', 'order_datetime')
    fields = ('total_price', ('user_id', 'order_id'), 'order_datetime')
    readonly_fields = ('product_id', 'user_id')



@admin.register(BaseUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_active', 'is_staff' )
    fields = ('image', 'username', ('first_name', 'last_name'), ('is_staff', 'is_active'), 'email', 'date_joined')
    readonly_fields = ('is_staff', 'is_active', 'username', 'email')
    search_fields = ('username', 'email', )

# Register your models here.

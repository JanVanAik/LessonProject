from django.contrib import admin
from mainapp.models import BaseUser, Order, Product


admin.site.register(BaseUser)
admin.site.register(Product)
admin.site.register(Order)
# Register your models here.

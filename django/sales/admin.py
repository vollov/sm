from django.contrib import admin

from .models import Product, Customer, ProductOrder, Order

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(ProductOrder)
admin.site.register(Order)
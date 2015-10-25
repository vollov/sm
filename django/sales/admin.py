from django.contrib import admin

from .models import Product, Customer, ProductOrder, Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','code','purchase_price','sell_price','market_price','created','active']
        
class CustomerAdmin(admin.ModelAdmin):      
    list_display = ['name','sin','address', 'phone', 'agent', 'created','active']    
    list_filter = ['agent']
    
class ProductOrderAdmin(admin.ModelAdmin):      
    list_display = ['product','amount', 'agent', 'order','created']    
    list_filter = ['agent']
    
    
class ProductOrderInline(admin.TabularInline):
    model = ProductOrder
    extra = 3
    
class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductOrderInline]
     
    list_display = ['id','store', 'agent', 'created']    
    list_filter = ['agent']
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(ProductOrder,ProductOrderAdmin)
admin.site.register(Order, OrderAdmin)

from django.contrib import admin

from models import Store, Product, Agent, Customer, ProductOrder, Order, ShippingAddress

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class AgentInline(admin.StackedInline):
    model = Agent
    can_delete = False
    verbose_name_plural = 'agents'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (AgentInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class StoreAdmin(admin.ModelAdmin):
    
    def activate(self, request, queryset):
        rows_updated = queryset.update(active=True)
        
        if rows_updated == 1:
            message_bit = "1 store was"
        else:
            message_bit = "%s store were" % rows_updated
        self.message_user(request, "%s successfully activated." % message_bit)
    
    activate.short_description = "Activate Stores"

    actions = [activate]
    list_display = ['id','name','code','currency_rate','tax_rate','agent_share','created_at']
    exclude = ('created_at', 'updated_at',)

admin.site.register(Store, StoreAdmin)

class ProductAdmin(admin.ModelAdmin):
     
    list_display = ['name','sku','purchase_price','sell_price','market_price','created_at','active']
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ['name', 'sku', 'note', 'desc']
    exclude = ('created_at', 'updated_at',)
    
admin.site.register(Product, ProductAdmin)

class ProductOrderAdmin(admin.ModelAdmin):      
    list_display = ['product','quantity', 'agent', 'order','created_at']
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ['name', 'agent','order','created_at']
    exclude = ('created_at', 'updated_at','agent','purchase_price','sell_price',)
    
    list_filter = ['agent','order','created_at']
    
admin.site.register(ProductOrder,ProductOrderAdmin)
    
class ProductOrderInline(admin.TabularInline):
    model = ProductOrder
    extra = 3
    exclude = ('created_at', 'updated_at','agent','purchase_price','sell_price',)
    
class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductOrderInline]
    ordering = ['-created_at']
    search_fields = ['name', 'agent','ship_to','delivery_company','created_at']
    list_display = ['id', 'agent', 'ship_to','delivery_cost','delivery_company','created_at']    
    list_filter = ['agent','ship_to','delivery_company','created_at']
    exclude = ('currency_rate','tax_rate','agent_share',)
    
admin.site.register(Order, OrderAdmin)

class CustomerAdmin(admin.ModelAdmin):      
    list_display = ['name','sin','address', 'phone', 'agent', 'created_at','active']    
    list_filter = ['agent']
    search_fields = ['name', 'agent']
    
admin.site.register(Customer, CustomerAdmin)

class ShippingAddressAdmin(admin.ModelAdmin):      
    list_display = ['name','sin','address', 'phone', 'created_at','active']    
    list_filter = ['agent']
    search_fields = ['name', 'address','agent']
    
admin.site.register(ShippingAddress, ShippingAddressAdmin)


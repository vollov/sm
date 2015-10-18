from django.contrib import admin

from models import Store, StoreEnrollment

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
    list_display = ['id','name', 'created', 'active']   

class StoreEnrollmentAdmin(admin.ModelAdmin):
    list_display = ['id','created', 'active']   

admin.site.register(Store, StoreAdmin)
admin.site.register(StoreEnrollment, StoreEnrollmentAdmin)

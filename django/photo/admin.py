from django.contrib import admin
from models import Image

class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('image_thumb',)
    search_fields = ["name"]
    list_display = ['id', 'product','name', 'weight','image_thumb', 'user','created', 'active']
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Image, ImageAdmin)
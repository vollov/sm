from django.contrib import admin
from django.utils.text import slugify
from models import Album, Image

import logging
logger = logging.getLogger(__name__)

class AlbumAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'slug','created', 'active']
    prepopulated_fields = {'slug': ('name',)}
    
    def save_model(self, request, obj, form, change):
        '''
        Replace all '-' with '_' in the slug
        ''' 
        logger.debug('album admin model save')
        
        obj.slug = slugify(form.cleaned_data['slug']).replace('-','_')
        obj.save()

admin.site.register(Album, AlbumAdmin)

class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('image_thumb',)
    search_fields = ["album"]  
    
    
    list_display = ['image_key', 'album','name', 'image_thumb', 'created', 'active']
     
admin.site.register(Image, ImageAdmin)

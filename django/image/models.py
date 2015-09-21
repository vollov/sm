from django.db import models
from django.conf import settings

import os, uuid

import logging
logger = logging.getLogger(__name__)

class Album(models.Model):
    """
    TODO:
    
    1. delete album, no break links
    """
    name = models.CharField(max_length=60, db_index=True, unique=True)
    weight = models.IntegerField(default=0)
    slug = models.SlugField(max_length=150, unique=True)
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        """
        Create a album folder in settings.MEDIA_ROOT, before save 
        a new album into database.
        """
        logger.debug('album model save {0}'.format(__name__))
        
        album_directory = os.path.join(settings.MEDIA_ROOT, self.slug)
        if not os.path.exists(album_directory):
            os.makedirs(album_directory)
     
        super(Album, self).save(*args, **kwargs)
        
    def __unicode__(self):
        return self.name

from storage import OverwriteStorage

def image_upload_path(instance, filename):
    ''' 
    build image upload path
    e.g.
    upload_path = album_name/f47ac10b-58cc-4372-a567-0e02b2c3d479.jpg
    '''
    file_extension = filename.split('.')[-1]
    saved_name = "{}.{}".format(instance.image_key, file_extension)
    return os.path.join(str(instance.album), saved_name)

class Image(models.Model):
    """
    TODO list here
    """
    name = models.CharField(max_length=60, blank=True, null=True)
    #f47ac10b-58cc-4372-a567-0e02b2c3d479.jpg
    image_key = models.CharField(max_length=64, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    album = models.ForeignKey('Album')
    image = models.ImageField(storage=OverwriteStorage(), upload_to=image_upload_path)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    def image_thumb(self):
        """read only field for display in administration UI"""
        return '<img src="/media/%s" width="100" height="100" />' % (self.image)
     
    image_thumb.allow_tags = True
        
    def __unicode__(self):
        return self.image.name
    
# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete, pre_save, post_delete
from django.dispatch.dispatcher import receiver

import shutil
@receiver(post_delete, sender=Album)
def auto_delete_album_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding Album object is deleted.
    """
    album_directory = os.path.join(settings.MEDIA_ROOT, instance.slug)
    if os.path.exists(album_directory):
        logger.debug('album on delete trigger delete folder {0}'.format(album_directory))
        shutil.rmtree(album_directory)
    
@receiver(pre_delete, sender=Image)
def auto_delete_image_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding Image object is deleted.
    """
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)

@receiver(pre_save, sender=Image)
def auto_delete_image_on_change(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding Image object is changed.
    """
    logger.debug('image on delete file {0}'.format(instance.image))
    if not instance.id:
        return False
 
    try:
        old_file = Image.objects.get(pk=instance.id).image
    except Image.DoesNotExist:
        return False
 
    new_file = instance.image
    if not old_file == new_file:
        old_file.delete(False)

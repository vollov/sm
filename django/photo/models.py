from django.db import models
from django.contrib.auth.models import User
from sales.models import Product
from storage import OverwriteStorage
import uuid,os

def image_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    saved_name = "{}.{}".format(instance.id, ext)
    return os.path.join(str(instance.product.id), saved_name)

class Image(models.Model):
    
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    name = models.CharField(max_length=60, blank=True, null=True)
    
    title = models.CharField(max_length=60, blank=True, null=True)
    #image = models.FileField(upload_to="images/")
    image = models.ImageField(storage=OverwriteStorage(), upload_to=image_upload_path)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True)
    
    product = models.ForeignKey(Product, null=True)
    is_thumbnail = models.BooleanField(default=False)
        
    def image_thumb(self):
        return '<img src="/media/%s" width="100" height="100" />' % (self.image)
     
    image_thumb.allow_tags = True
    
    def __unicode__(self):
        return self.image.name
    
# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete, pre_save
from django.dispatch.dispatcher import receiver

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
    ## used to be instance.pk
    if not instance.id:
        return False
 
    try:
        old_file = Image.objects.get(pk=instance.id).image
    except Image.DoesNotExist:
        return False
 
    new_file = instance.image
    if not old_file == new_file:
        old_file.delete(False)
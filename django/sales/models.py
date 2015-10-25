from django.db import models

from decimal import *
import uuid, os

from django.contrib.auth.models import User
from store.models import Store
from django.conf import settings

# class CurrencyRate(models.Model):
#     rate = models.DecimalField(max_digits=9, decimal_places=4, blank=False, null=False)
#     created = models.DateTimeField(auto_now_add=True)
#     active = models.BooleanField(default=True)
# 
#     def __unicode__(self):
#         return self.rate
    
class Product(models.Model):
    """
    display price:
    
    1) return ratio
    2) 13% tax
    3) after Tax price
    2) purchase price in RMB
    """
    
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    
    name = models.CharField(max_length=60, blank=True, null=True)
    code = models.CharField(max_length=8, blank=True, null=True)
    
    #CAD
    purchase_price = models.DecimalField(max_digits=9, decimal_places=4)
    
    #RMB
    sell_price = models.DecimalField(max_digits=9, decimal_places=4)
    
    #RMB
    market_price = models.DecimalField(max_digits=9, decimal_places=4)
    
    desc = models.CharField(max_length=125, blank=True, null=True)
    
    note = models.CharField(max_length=125, blank=True, null=True)
    
    store = models.ForeignKey(Store, null=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    # Before save to db, create album folder in settings.MEDIA_ROOT, 
    # if the folder is not existing
    def save(self, *args, **kwargs):
        album_directory = os.path.join(settings.MEDIA_ROOT, self.id)
        
        if not os.path.exists(album_directory):
            os.makedirs(album_directory)
    
        super(Product, self).save(*args, **kwargs)
        
    def __unicode__(self):
        return str(self.name)

class Customer(models.Model):
    
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    name = models.CharField(max_length=16, blank=True, null=True)
    sin = models.CharField(max_length=24, blank=True, null=True)
    address = models.CharField(max_length=125, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    
    product_orders = models.ManyToManyField(Product, related_name='product_orders', through='ProductOrder')
    
    # owner of the customer
    agent = models.ForeignKey(User, null=True)
    store = models.ForeignKey(Store, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return str(self.name)
    
class Order(models.Model):
    """
    display: prime_price = procudt.purchase_price x 1.13 x rate
    
    many to many with Customer and ProductOrder
    """
    
    CLOSED = 'F'    #Closed
    SHIPPING = 'S'         #Shipping
    CONFIRMED = 'Y'         #Confirmed
    CANCEL = 'X'         #Cancel
    
    # TRANSMISSION: Automatic,MANUAL,other
    ORDER_STATUS_CHOICE = (
        (CLOSED, 'Closed'),
        (SHIPPING, 'Shipping'),
        (CONFIRMED, 'Confirmed'),
        (CANCEL, 'Cancel'),
    )
    
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    
    created = models.DateTimeField(auto_now_add=True)
    
    store = models.ForeignKey(Store, null=True)
    agent = models.ForeignKey(User, null=True)
    delivery_cost = models.DecimalField(max_digits=9, decimal_places=4, default=0)
    status = models.CharField(max_length=2,
                                      choices=ORDER_STATUS_CHOICE,
                                      default=CONFIRMED)
    
    def __unicode__(self):
        return str(self.id)
    
class ProductOrder(models.Model):
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    product = models.ForeignKey(Product, null=True)
    customer = models.ForeignKey(Customer, null=True)
    order = models.ForeignKey(Order, null=True)
    # additional
    amount = models.IntegerField(default=0)
    store = models.ForeignKey(Store, null=True)
    agent = models.ForeignKey(User, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return str(self.id)
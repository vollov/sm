from django.db import models

from decimal import *

class CurrencyRate(models.Model):
    rate = models.DecimalField(max_digits=9, decimal_places=4, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.rate
    
class Product(models.Model):
    """
    display price:
    
    1) return ratio
    2) 13% tax
    3) after Tax price
    2) purchase price in RMB
    """
    
    id = models.CharField(max_length=64, verbose_name=u"Activation key",
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
    
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name

class Customer(models.Model):
    
    id = models.CharField(max_length=64, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    name = models.CharField(max_length=16, blank=True, null=True)
    sin = models.CharField(max_length=24, blank=True, null=True)
    address = models.CharField(max_length=125, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    
    def __unicode__(self):
        return self.name

class ProductOrder(models.Model):
    product = models.ForeignKey('Product')
    amount = models.IntegerField(default=0)
    order = models.ForeignKey('Order')

class Order(models.Model):
    """
    display: prime_price = procudt.purchase_price x 1.13 x rate
    
    """
    
    CLOSED = 'F'    #Closed
    PROCESSING = 'P'         #Processing
    WAIT_CONFIRM = 'W'         #Waiting Confirm
    CANCEL = 'C'         #Cancel
    
    # TRANSMISSION: Automatic,MANUAL,other
    ORDER_STATUS_CHOICE = (
        (CLOSED, 'Automatic'),
        (PROCESSING, 'Manual'),
        (WAIT_CONFIRM, 'Waiting Confirm'),
        (CANCEL, 'Cancel'),
    )
    
    id = models.CharField(max_length=64, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    
    created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey('Product')
    status = models.CharField(max_length=2,
                                      choices=ORDER_STATUS_CHOICE,
                                      default=WAIT_CONFIRM)
    
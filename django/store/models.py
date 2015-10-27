from django.db import models
from django.contrib.auth.models import User
import uuid


class Store(models.Model):
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    name = models.CharField(max_length=60, unique=True, null=True)
    code = models.CharField(max_length=10, unique=True, null=True)
    # canadian dollar to RMB rate
    currency_rate = models.DecimalField(max_digits=9, decimal_places=4, default=5, blank=False, null=False)
    tax_rate = models.DecimalField(max_digits=9, decimal_places=4, default=0.13, blank=False, null=False)

    agent_share = models.DecimalField(max_digits=9, decimal_places=4, default=0.4, blank=False, null=False)
    
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name
    
# class Product(models.Model):
#     """
#     display price:
#     
#     1) return ratio
#     2) 13% tax
#     3) after Tax price
#     2) purchase price in RMB
#     """
#     
#     id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
#                  default=uuid.uuid4)
#     
#     name = models.CharField(max_length=250, blank=True, null=True)
#     code = models.CharField(max_length=8, blank=True, null=True)
#     
#     #CAD
#     purchase_price = models.DecimalField(max_digits=9, decimal_places=4)
#     
#     #RMB
#     sell_price = models.DecimalField(max_digits=9, decimal_places=4)
#     
#     #RMB
#     market_price = models.DecimalField(max_digits=9, decimal_places=4)
#     
#     desc = models.TextField(blank=True, null=True)
#     
#     note = models.CharField(max_length=125, blank=True, null=True)
#     
#     store = models.ForeignKey(Store, null=True)
#     created = models.DateTimeField(auto_now_add=True)
#     active = models.BooleanField(default=True)
#     
#     # Before save to db, create album folder in settings.MEDIA_ROOT, 
#     # if the folder is not existing
#     def save(self, *args, **kwargs):
#         album_directory = os.path.join(settings.MEDIA_ROOT, self.id)
#         
#         if not os.path.exists(album_directory):
#             os.makedirs(album_directory)
#     
#         super(Product, self).save(*args, **kwargs)
#         
#     def __unicode__(self):
#         return self.name
# 
# class Customer(models.Model):
#     
#     id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
#                  default=uuid.uuid4)
#     name = models.CharField(max_length=16, blank=True, null=True)
#     sin = models.CharField(max_length=24, blank=True, null=True)
#     address = models.CharField(max_length=125, blank=True, null=True)
#     phone = models.CharField(max_length=10, blank=True, null=True)
#     
#     product_orders = models.ManyToManyField(Product, related_name='product_orders', through='ProductOrder')
#     
#     # owner of the customer
#     agent = models.ForeignKey(User, null=True)
#     store = models.ForeignKey(Store, null=True)
#     created = models.DateTimeField(auto_now_add=True, blank=True)
#     active = models.BooleanField(default=True)
#     
#     def __unicode__(self):
#         return self.name
#     
# class Order(models.Model):
#     """
#     display: prime_price = procudt.purchase_price x 1.13 x rate
#     
#     many to many with Customer and ProductOrder
#     """
#     
#     CLOSED = 'F'    #Closed
#     SHIPPING = 'S'         #Shipping
#     CONFIRMED = 'Y'         #Confirmed
#     CANCEL = 'X'         #Cancel
#     
#     # TRANSMISSION: Automatic,MANUAL,other
#     ORDER_STATUS_CHOICE = (
#         (CLOSED, 'Closed'),
#         (SHIPPING, 'Shipping'),
#         (CONFIRMED, 'Confirmed'),
#         (CANCEL, 'Cancel'),
#     )
#     
#     id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
#                  default=uuid.uuid4)
#     
#     created = models.DateTimeField(auto_now_add=True)
#     
#     store = models.ForeignKey(Store, null=True)
#     agent = models.ForeignKey(User, null=True)
#     delivery_cost = models.DecimalField(max_digits=9, decimal_places=4, default=0)
#     status = models.CharField(max_length=2,
#                                       choices=ORDER_STATUS_CHOICE,
#                                       default=CONFIRMED)
#     
#     def __unicode__(self):
#         return str(self.id)
#     
# class ProductOrder(models.Model):
#     id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
#                  default=uuid.uuid4)
#     product = models.ForeignKey(Product, null=True)
#     customer = models.ForeignKey(Customer, null=True)
#     order = models.ForeignKey(Order, null=True)
#     # additional
#     # keep a copy of history purchase/sales price
#     sell_price = models.DecimalField(max_digits=9, decimal_places=4,default=0)
#     purchase_price = models.DecimalField(max_digits=9, decimal_places=4,default=0)
#     amount = models.IntegerField(default=0)
#     store = models.ForeignKey(Store, null=True)
#     agent = models.ForeignKey(User, null=True)
#     created = models.DateTimeField(auto_now_add=True)
#     
#     def save(self, *args, **kwargs):
#         """
#         auto update the sell_price and purchase_price.
#         """
#         self.sell_price = self.product.sell_price
#         self.purchase_price = self.product.purchase_price
#         
#         super(ProductOrder, self).save(*args, **kwargs)
#         
#     def __unicode__(self):
#         return str(self.id)
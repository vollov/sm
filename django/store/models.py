from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import uuid, os, decimal

class Agent(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=16)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'agents'
        
class Store(models.Model):
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    name = models.CharField(max_length=60, unique=True, null=True)
    code = models.CharField(max_length=10, unique=True, null=True)
    # canadian dollar to RMB rate
    currency_rate = models.DecimalField(max_digits=9, decimal_places=2, default=5.50, blank=False, null=False)
    tax_rate = models.DecimalField(max_digits=9, decimal_places=2, default=0.13, blank=False, null=False)

    agent_share = models.DecimalField(max_digits=9, decimal_places=2, default=0.4, blank=False, null=False)
    
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.CharField(max_length=255, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return u'' + self.name
    
    class Meta:
        db_table = 'stores'
        
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
     
    name = models.CharField(max_length=255, blank=True, null=True)
    
    #stockkeeping unit - used in url as slug
    sku = models.CharField(max_length=64, unique=True)
     
    #CAD
    purchase_price = models.DecimalField(max_digits=9, decimal_places=2)
    
    #RMB
    sell_price = models.DecimalField(max_digits=9, decimal_places=2)
     
    #RMB
    market_price = models.DecimalField(max_digits=9, decimal_places=2)
     
    desc = models.TextField(blank=True, null=True)
     
    note = models.CharField(max_length=125, blank=True, null=True)
     
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
     
    # Before save to db, create album folder in settings.MEDIA_ROOT, 
    # if the folder is not existing
    def save(self, *args, **kwargs):
        album_directory = os.path.join(settings.MEDIA_ROOT, self.id)
        
        if not os.path.exists(album_directory):
            os.makedirs(album_directory)
     
        super(Product, self).save(*args, **kwargs)
         
    def __unicode__(self):
        return u'({0})-{1}'.format(self.sku,self.name)
 
    class Meta:
        db_table = 'products'
        ordering = ['-created_at']
        
class Customer(models.Model):
     
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    name = models.CharField(max_length=16, blank=True, null=True)
    sin = models.CharField(max_length=24, blank=True, null=True)
    address = models.CharField(max_length=125, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
     
    product_orders = models.ManyToManyField(Product, related_name='product_orders', through='ProductOrder')
     
    # owner of the customer
    agent = models.ForeignKey(User, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
     
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'customer'
        ordering = ['-created_at']
        
class ShippingAddress(models.Model):
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    
    sin = models.CharField(max_length=24, blank=True, null=True)
    name = models.CharField(max_length=16, unique=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True)
    postcode = models.CharField(max_length=10, blank=True, null=True)
    
    agent = models.ForeignKey(User, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'shipping_address'
        ordering = ['-created_at']
    
    def __unicode__(self):
        return self.name
    
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
     
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    agent = models.ForeignKey(User, null=True)
    store = models.ForeignKey(Store, null=True)
    
    delivery_company = models.CharField(max_length=255, blank=True, null=True)
    tarcking_code = models.CharField(max_length=255, blank=True, null=True)
    
    ship_to = models.ForeignKey(ShippingAddress, null=True)
    delivery_cost = models.DecimalField(max_digits=9, decimal_places=3, default=0.0)
    status = models.CharField(max_length=2,
                                      choices=ORDER_STATUS_CHOICE,
                                      default=CONFIRMED)
    
    # kept history data here
    currency_rate = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    tax_rate = models.DecimalField(max_digits=9, decimal_places=2,null=True)
    agent_share = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    
    def save(self, *args, **kwargs):
        """
        auto update 'currency_rate','tax_rate','agent_share',.
        """
        if not self.currency_rate:
            self.currency_rate = self.store.currency_rate
            
        if not self.tax_rate:
            self.tax_rate = self.store.tax_rate
            
        if not self.agent_share:
            self.agent_share = self.store.agent_share
         
        super(Order, self).save(*args, **kwargs)
        
    def __unicode__(self):
        return str(self.id)
     
    class Meta:
        db_table = 'orders'
        ordering = ['-created_at']
    
    @property
    def gross_profit(self):
        total = decimal.Decimal('0.00')
        order_items = ProductOrder.objects.filter(order=self)
        for item in order_items:
            total += item.profit_total
        return total
    
    @property
    def purchase_total(self):
        total = decimal.Decimal('0.00')
        order_items = ProductOrder.objects.filter(order=self)
        for item in order_items:
            total += item.purchase_total
        return total
    
    @property
    def net_profit(self):
        return self.gross_profit - self.delivery_cost
    
    @property
    def agent_profit(self):
        return self.net_profit * self.agent_share
    
    @property
    def owner_profit(self):
        return self.net_profit - self.agent_share
    
    @property
    def agent_payment(self):
        return self.purchase_total + self.delivery_cost + self.owner_profit
        
class ProductOrder(models.Model):
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    product = models.ForeignKey(Product, null=True)
    customer = models.ForeignKey(Customer, null=True)
    order = models.ForeignKey(Order, null=True)

    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     
    # keep a copy of history purchase/sales price
    sell_price = models.DecimalField(max_digits=9, decimal_places=2,default=None)
    purchase_price = models.DecimalField(max_digits=9, decimal_places=2,default=None)
    
    class Meta:
        db_table = 'product_orders'
        ordering = ['-created_at']
     
    @property
    def sell_total(self):
        return round(self.quantity * self.product.sell_price, 2)
    
    @property
    def purchase_total(self):
        return round(self.quantity * self.unit_cost, 2)
    
    @property
    def profit_total(self):
        return round(self.quantity * self.unit_profit, 2)
    
    @property
    def unit_profit(self):
        return round(self.product.sell_price - decimal.Decimal(self.unit_cost), 2)
    
    @property
    def unit_cost(self):
        return round(self.product.purchase_price * self.order.currency_rate * (1 + self.order.tax_rate), 2)
    
    @property
    def name(self):
        return self.product.name
    
    @property
    def sku(self):
        return self.product.sku    
    
    def save(self, *args, **kwargs):
        """
        auto update the sell_price and purchase_price.
        """
        if not self.sell_price:
            self.sell_price = self.product.sell_price
            
        if not self.purchase_price:
            self.purchase_price = self.product.purchase_price
         
        super(ProductOrder, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return str(self.id)
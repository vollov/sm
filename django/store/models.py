from django.db import models
from django.contrib.auth.models import User
import uuid


class Store(models.Model):
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    name = models.CharField(max_length=60, unique=True, null=True)
    # a user can have only one store
    owner = models.ForeignKey(User)
    sales = models.ManyToManyField(User, related_name='sales', through='StoreEnrollment')
    # canadian dollar to RMB rate
    currency_rate = models.DecimalField(max_digits=9, decimal_places=4, default=5, blank=False, null=False)
    currency_type =  models.CharField(max_length=3, default='CAD', null=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name

class StoreEnrollment(models.Model):
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    agent = models.ForeignKey(User)
    store = models.ForeignKey(Store)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.store.name + '_' + self.agent.username
    
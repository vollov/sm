from django.db import models
from django.contrib.auth.models import User
import uuid

class Store(models.Model):
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    name = models.CharField(max_length=60, unique=True, null=True)
    owner = models.ForeignKey(User)
    sales = models.ManyToManyField(User)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name
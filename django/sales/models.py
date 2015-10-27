# -*- coding: utf-8 -*-

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
    

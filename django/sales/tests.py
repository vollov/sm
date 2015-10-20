from django.test import TestCase

# Test models
from .models import Product, Order
from django.contrib.auth.models import User
   
class ProductTestCase(TestCase):
    fixtures = ['user.json', 'store.json']
    
    def test_create_store(self):
        """user anna can create store"""
        
class OrderTestCase(TestCase):
    fixtures = ['user.json', 'store.json']
    
    def test_create_store(self):
        """user anna can create store"""
#         anna = User.objects.get(username='anna')
#         
#         store = Store(name="Anna Fish Store")
#         store.owner = anna
#         store.save()
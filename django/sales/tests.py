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


## test suits for forms ##
from .forms import CustomerForm

class CustomerFormTestCase(TestCase):
    
    def test_forms(self):
        form_data = {'name': 'martin zhang',
                     'sin':'11223344556677',
                     'address':'king st, kitchener, ontario',
                     'phone':'519-616-1234'}
        
        customer_form = CustomerForm(data=form_data)
        
        if not customer_form.is_valid():
            print customer_form.errors
        else:
            self.assertTrue(customer_form.is_valid())
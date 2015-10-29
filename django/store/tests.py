from django.test import TestCase

# Test models
from models import Product, Order, ProductOrder
from django.contrib.auth.models import User

class TestProductModel(TestCase):
    """test product model"""
    
    fixtures = ['auth.json', 'store.json']
    
    def test_list_product(self):
        """Product can be listed"""
        products = Product.objects.filter(active=True)
#         for p in products:
#             print (p.created_at)
        
        expected_number = 3
        self.assertEqual(len(products), expected_number, 'number of products should be '+ str(expected_number))
        
class TestProductOrderModel(TestCase):
    """test product order model"""
    
    fixtures = ['auth.json', 'store.json']
    
    def setUp(self):
        self.product_order = ProductOrder.objects.get(id='')
        
         
    def test_sell_total(self):
        expected_sell_total = 0
        
    def test_purchase_total(self):
        expected_purchase_total = 0
        
    def test_profit_total(self):
        expected_number = 2
        self.assertEqual(len(products), expected_number, 'number of products should be '+ str(expected_number))
        
    def test_unit_profit(self):
        
    def test_unit_cost(self):
        
    def test_sku(self):
        
        
        
# class StoreTestCase(TestCase):
#     fixtures = ['user.json', 'store.json']
#     
#     def test_create_store(self):
#         """user anna can create store"""
#         anna = User.objects.get(username='anna')
#         
#         store = Store(name="Anna Fish Store")
#         store.owner = anna
#         store.save()
#         
#     def test_join_store(self):
#         """user martin can join store"""
#         martin = User.objects.get(username='martin')
#         store = Store.objects.get(name='Kate Store')
#         
#         enroll = StoreEnrollment(agent=martin, store=store)
#         enroll.save()
#         
#     def test_approve_join(self):
#         """owner can approve join store request"""
#         anna = User.objects.get(username='anna')
#         store = Store.objects.get(name='Kate Store')
#         enroll = StoreEnrollment.objects.get(agent=anna, store=store)
#         
#         enroll.active=True
#         enroll.save()
#         
#     def test_add_product(self):
#         """owner can add products"""
        
# from pprint import pprint
# from .views import ProfileViewHelper
# 
# class ProfileViewHelperTestCase(TestCase):
#     fixtures = ['user.json', 'store.json', 'sales.json']
#     
#     def setUp(self):
#         print 'ProfileViewHelperTestCase.setUp()'
#         
#     def test_get_owned_stores(self):
#         """test owner kate profile"""
#         kate = User.objects.get(username='kate')
#         
#         profileViewHelper = ProfileViewHelper(kate)
# #         profileViewHelper.direct_view(request)
#         store = profileViewHelper.get_owned_stores()
#         
#         expected_store_name = 'Kate Store'
#         self.assertEqual(store.name,expected_store_name,'name of the store should be '+ expected_store_name)
#         
#     def test_get_joined_stores(self):
#         """test agent anna login"""
#         anna = User.objects.get(username='anna')
#         
#         profileViewHelper = ProfileViewHelper(anna)
# #         profileViewHelper.direct_view(request)
#         store = profileViewHelper.get_joined_stores()
#         
#         expected_store_name = 'Kate Store'
#         self.assertEqual(store.name,expected_store_name,'name of the store should be '+ expected_store_name)
    
        
   
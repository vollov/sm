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
        self.product_order = ProductOrder.objects.get(id='7540a9e1-1b1a-44c7-8dee-e02056916aa1')
        
         
    def test_sell_total(self):
        expected_sell_total = 300.00
        self.assertEqual(self.product_order.sell_total, expected_sell_total, 'sell total should be '+ str(expected_sell_total))
           
    def test_purchase_total(self):
        expected_purchase_total = 248.60
        print 'self.product_order.purchase_total={0}'.format(str(self.product_order.purchase_total))
        
        self.assertEqual(self.product_order.purchase_total, expected_purchase_total, 'purchase total should be '+ str(expected_purchase_total))
        
         
    def test_profit_total(self):
        expected_profit_total = 51.40
        print 'self.product_order.profit_total={0}'.format(str(self.product_order.profit_total))
        self.assertEqual(self.product_order.profit_total, expected_profit_total, 'profit total should be '+ str(expected_profit_total))
        
         
    def test_unit_profit(self):
        expected_unit_profit = 25.70
        self.assertEqual(self.product_order.unit_profit, expected_unit_profit, 'unit profit should be '+ str(expected_unit_profit))
        
    def test_unit_cost(self):
        """self.product.purchase_price * self.order.currency_rate * (1 + self.order.tax_rate)"""
        
        expected_unit_cost = 124.30
        #" {0:.2f}
        print 'self.product_order.unit_cost={0}'.format(str(self.product_order.unit_cost))
        self.assertEqual(self.product_order.unit_cost, expected_unit_cost, 'product unit cost should be '+ str(expected_unit_cost))
    
    def test_sku(self):
        expected_sku = '10001'
        self.assertEqual(self.product_order.sku, expected_sku, 'product sku should be '+ expected_sku)
        
        
class TestOrderModel(TestCase):
    """test product order model
    
    (180 - (20*5.5*1.13)) *1 = 55.70
    (150 - (20*5.5*1.13))*2 = (150-124.3)*2= 51.4
    
    gp = 107.1
    np = 107.1-55 = 52.1
    ap = 52.1 *0.4 = 20.84
    """
    
    fixtures = ['auth.json', 'store.json']
    
    def setUp(self):
        self.order = Order.objects.get(id='78c5b842-7540-4d82-8d87-da4f8ec6af58')
      
    def test_purchase_total(self):
        expected_purchase_total = 372.90
        self.assertEqual(self.order.purchase_total, expected_purchase_total, 'purchase total should be '+ str(expected_purchase_total))
    
    def test_gross_profit(self):
        expected_gross_profit = 107.1
        print 'self.order.gross_profit={0}'.format(str(self.order.gross_profit))
        self.assertEqual(self.order.gross_profit, expected_gross_profit, 'net profit should be '+ str(expected_gross_profit))
     
    def test_net_profit(self):
        """ 107.1 - 55"""
        expected_net_profit = 52.1
        print 'self.order.net_profit={0}'.format(str(self.order.net_profit))
        self.assertEqual(self.order.net_profit, expected_net_profit, 'net profit should be '+ str(expected_net_profit))
        
    def test_agent_profit(self):
        expected_agent_profit = 20.84
        print 'self.order.agent_profit={0}'.format(str(self.order.agent_profit))
        self.assertEqual(self.order.agent_profit, expected_agent_profit, 'purchase total should be '+ str(expected_agent_profit))
     
    def test_owner_profit(self):
        expected_owner_profit = 31.26
        print 'self.order.owner_profit={0}'.format(str(self.order.owner_profit))
        self.assertEqual(self.order.owner_profit, expected_owner_profit, 'owner profit should be '+ str(expected_owner_profit))
     
    def test_agent_payment(self):
        """ agent payment = 372.90 + 55 + 31.26"""
        expected_agent_payment = 459.16
        print '{0} ==== {1}'.format(type(expected_agent_payment),type(self.order.agent_payment))
        print 'self.order.agent_payment={0}'.format(str(self.order.agent_payment))
        self.assertEqual(self.order.agent_payment, expected_agent_payment, 'agent payment should be '+ str(expected_agent_payment))
       
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
    
        
   
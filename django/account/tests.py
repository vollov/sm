from django.test import TestCase

from account.forms import UserForm, UserProfileForm
from captcha.models import CaptchaStore

## test suits for models ##
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserModelTestCase(TestCase):
    def setUp(self):
        john = User.objects.create_user('john', 'john@abc.com', 'testpassword')
        eddy = User.objects.create_user('eddy', 'eddy@abc.com', 'testpassword')

    def test_user_auth(self):
        """user are correctly identified"""
        
        john = authenticate(username='john', password='testpassword')
        expected_email = 'john@abc.com'
        self.assertEqual(john.email,expected_email,'email for test_user_auth should be john@abc.com')
        self.assertTrue(john.is_active,'user john should be active')
        
class UserFixtureTestCase(TestCase):
    """Test user model with fixture"""
    
    fixtures = ['user.json', 'store.json']
    
    def setUp(self):
        print 'UserTestCase.setUp()'
        
    def test_user_auth(self):
        """user are correctly identified"""
        
        martin = authenticate(username='martin', password='testpassword')
        expected_email = 'martin@abc.com'
        
        self.assertEqual(martin.email,expected_email,'email for martin should be '+ expected_email)
        self.assertTrue(martin.is_active,'user martin should be active')
        
     
## test suits for forms ##

class TestUserForm(TestCase):
    def test_forms(self):
        form_data = {'username': 'martin',
                     'email':'martin@abc.com',
                     'password':'pwd123',
                     'captcha_0':'dummy-value',
                     'captcha_1':'PASSED'}
        user_form = UserForm(data=form_data)
        
        if not user_form.is_valid():
            print user_form.errors
        else:
            self.assertTrue(user_form.is_valid())
    
     
## test suits for views ##
from django.test import Client
from django.core.urlresolvers import reverse

class TestLoginView(TestCase):
    
    fixtures = ['user.json', 'store.json']
    
    def setUp(self):
        print 'TestLoginView.setUp()'
        self._client = Client()
        
    def test_owner_login(self):
        
#         self._client.post('/account/login/', {'username': 'kate', 'password': 'testpassword'})
#         response = self.client.get('/store/owner/')

#         self.assertRedirects(response, expected_url=reverse('account.views.sign_in'), status_code=302, target_status_code=200)
        
        response = self._client.post('/account/login/', {'username': 'kate', 'password': 'testpassword'})
        expected_status_code = 200
        self.assertEqual(response.status_code, expected_status_code,'response status code should be 200')
        #print response.status_code

        #print 'page_title= {0}'.format(response.context['page_title'])    
        expected_page_title = 'Owner profile'
        self.assertEqual(response.context['page_title'], expected_page_title,'page title should be ' +  expected_page_title)

    def test_agent_login(self):        
        response = self._client.post('/account/login/', {'username': 'skyler', 'password': 'testpassword'})
        expected_status_code = 200
        self.assertEqual(response.status_code, expected_status_code,'response status code should be 200')
        #print response.status_code
 
        #print 'page_title= {0}'.format(response.context['page_title'])    
        expected_page_title = 'Agent profile'
        self.assertEqual(response.context['page_title'], expected_page_title,'page title should be ' +  expected_page_title)
           
    def test_unapproved_agent_login(self):        
        response = self._client.post('/account/login/', {'username': 'anna', 'password': 'testpassword'})
        expected_status_code = 200
        self.assertEqual(response.status_code, expected_status_code,'response status code should be 200')
        #print response.status_code

        #print 'page_title= {0}'.format(response.context['page_title'])    
        expected_page_title = 'Unapproved agent profile'
        self.assertEqual(response.context['page_title'], expected_page_title,'page title should be ' +  expected_page_title)
             
    def test_user_login(self):        
        response = self._client.post('/account/login/', {'username': 'martin', 'password': 'testpassword'})
        expected_status_code = 200
        self.assertEqual(response.status_code, expected_status_code,'response status code should be 200')
        #print response.status_code

        print 'page_title= {0}'.format(response.context['page_title'])    
        expected_page_title = 'User profile'
        self.assertEqual(response.context['page_title'], expected_page_title,'page title should be' +  expected_page_title)
         
# class UserProfileForm(TestCase):
#     def test_forms(self):
#         user_form_data = {'username': 'martin',
#                      'email':'martin@abc.com',
#                      'password':'pwd123',
#                      'captcha_0':'dummy-value',
#                      'captcha_1':'PASSED'}
#         
#         
#         form_data = {
#                     'phone': '5196667788',
#                      #'user':user
# #                      'username': 'martin',
# #                      'email':'martin@abc.com',
# #                      'password':'pwd123',
# #                      'captcha_0':'dummy-value',
# #                      'captcha_1':'PASSED'
#                      }
#         user_form = UserForm(data=user_form_data)
#         
#         profile_form = UserProfileForm(data=form_data)
#         
#         user = user_form.save(commit=False)
#         
#         if not profile_form.is_valid():
#             print profile_form.errors
#         else:
#             self.assertTrue(profile_form.is_valid())
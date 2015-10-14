from django.test import TestCase

from account.forms import UserForm, UserProfileForm
from captcha.models import CaptchaStore

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
            
class UserProfileForm(TestCase):
    def test_forms(self):
        user_form_data = {'username': 'martin',
                     'email':'martin@abc.com',
                     'password':'pwd123',
                     'captcha_0':'dummy-value',
                     'captcha_1':'PASSED'}
        
        
        form_data = {
                    'phone': '5196667788',
                     #'user':user
#                      'username': 'martin',
#                      'email':'martin@abc.com',
#                      'password':'pwd123',
#                      'captcha_0':'dummy-value',
#                      'captcha_1':'PASSED'
                     }
        user_form = UserForm(data=user_form_data)
        
        profile_form = UserProfileForm(data=form_data)
        
        user = user_form.save(commit=False)
        
        if not profile_form.is_valid():
            print profile_form.errors
        else:
            self.assertTrue(profile_form.is_valid())
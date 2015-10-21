from django import forms
from captcha.fields import CaptchaField

from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Button, Submit, ButtonHolder
from models import Customer

class CustomerForm(forms.ModelForm):
    
    name = forms.CharField(required=True, widget=forms.TextInput(
                    attrs={'class':'form-control',
                           'placeholder' :'Full Name',       
                    }))
    
    sin = forms.CharField(required=True, widget=forms.TextInput(
                    attrs={'class':'form-control',
                           'placeholder' :'4403017919xxxx',       
                    }))
    
    address = forms.CharField(required=True, widget=forms.TextInput(
                    attrs={'class':'form-control',
                           'placeholder' :'Address',       
                    }))
    
    phone = forms.CharField(required=True, widget=forms.TextInput(
                    attrs={'class':'form-control',
                           'placeholder' :'phone number',       
                    }))
    
    class Meta:
        model = Customer
        fields = ('name', 'sin', 'address', 'phone')

from django import forms
from captcha.fields import CaptchaField

from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Button, Submit, ButtonHolder
from models import Store

class StoreForm(forms.ModelForm):
    
    name = forms.CharField(required=True, widget=forms.TextInput(
                    attrs={'class':'form-control',
                           'placeholder' :'Store Name',       
                    }))
    
    class Meta:
        model = Store
        fields = ('name',)

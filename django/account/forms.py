from django import forms

from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(required=True, widget=forms.PasswordInput(
                    attrs={'class':'form-control',
                           'placeholder' :'Password',
                    }))
    captcha = CaptchaField()
    
    username = forms.CharField(required=True, widget=forms.TextInput(
                    attrs={'class':'form-control',
                           'placeholder' :'User Name',       
                    }))
    
    email = forms.EmailField(required=True,widget=forms.TextInput(
                    attrs={'class':'form-control',
                           'placeholder' :'name@gmail.com',       
                    }))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    phone = forms.CharField(required=True,widget=forms.TextInput(
                    attrs={'class':'form-control',
                           'placeholder' :'(416)-111-1234',
                    }))
        
    class Meta:
        model = UserProfile
        fields = ('phone',)
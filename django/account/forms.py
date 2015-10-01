from django import forms
from captcha.fields import CaptchaField

from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    captcha = CaptchaField()
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
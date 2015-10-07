from django import forms
from captcha.fields import CaptchaField

from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Button, Submit, ButtonHolder
from models import Store

class StoreForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
#         owner = kwargs.pop('user','')
        super(StoreForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field(
                'name',
                placeholder = 'Store Name',
                css_class="form-control",
            ),
#             Field('owner', type="hidden"),                                                                      
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn btn-lg btn-primary btn-block')
            )
            
        )
    
    class Meta:
        model = Store
        fields = ('name',)
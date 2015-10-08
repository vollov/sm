from django import forms

from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from store.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    captcha = CaptchaField()
    
#     def __init__(self, *args, **kwargs):
#         
#         super(UserForm, self).__init__(*args, **kwargs)
# #         self.fields['owner']
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Field(
#                 'username',
#                 placeholder = 'User Name',
#                 css_class="form-control",
#             ),
#             Field(
#                 'email',
#                 placeholder = 'name@gmail.com',
#                 css_class="form-control",
#             ),
#             Field(
#                 'password',
#                 placeholder = 'xxxxxxxx',
#                 css_class="form-control",
#             ),
#             Field(
#                 'captcha',
#                 css_class="form-control",
#             ),                                                                      
# #             ButtonHolder(
# #                 Submit('submit', 'Submit', css_class='btn btn-lg btn-primary btn-block')
# #             )
#             
#         )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    phone = forms.CharField(required=True)
    
#     def __init__(self, *args, **kwargs):
#         
#         super(UserProfileForm, self).__init__(*args, **kwargs)
# #         self.fields['owner']
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Field(
#                 'phone',
#                 placeholder = '(519)-xxx-xxxx',
#                 css_class="form-control",
#             ),                                                                 
# #             ButtonHolder(
# #                 Submit('submit', 'Submit', css_class='btn btn-lg btn-primary btn-block')
# #             )
#             
#         )
        
    class Meta:
        model = UserProfile
        fields = ('phone',)
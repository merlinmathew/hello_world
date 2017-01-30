from django import forms
__author__ = 'user'
#
# class LoginForm(forms.Form):
#     username = forms.CharField(error_messages = {'required': ""})
#     email=forms.EmailField(error_messages = {'required': ""})
#     password = forms.CharField(max_length=50, widget=forms.PasswordInput,error_messages = {'required': ""})

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    email=forms.EmailField(required=True)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput,required=True)

    def __init__(self, *args, **kwargs):
       super(LoginForm, self).__init__(*args, **kwargs)
       for field in self.fields:
           self.fields[field].widget.attrs['class'] = 'form-control'




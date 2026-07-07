from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from django import forms


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username'
        })

        self.fields['email'].widget.attrs.update({
            'placeholder': 'Email address'
        })

        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Password'
        })

        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Password confirmation'
        })

        for field in self.fields.values():
            field.help_text = ''
      
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
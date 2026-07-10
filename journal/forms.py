from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from django.forms import ModelForm
from django.forms.widgets import Textarea

from . models import Thought, Profile

class UpdateProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file file-uploader', 'type': 'file', 'onchange' : 'upload()', 
                                                                 'accept' : "image/*" }))
    class Meta:
        model = Profile 
        fields = ['profile_pic']
        
class ThoughtForm(ModelForm):
    class Meta:
        model = Thought
        fields = ['title', 'content']
        widgets = {
            'content': Textarea(attrs={
                'placeholder': 'Write your thought...',
                'rows': 5
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'placeholder': 'Title'
        })

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
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Username",
        }),
        label=""
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password",
        }),
        label=""
    )


class UpdateUserForm(forms.ModelForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'email']
        exclude = ['password','password1']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username'
        })

        self.fields['email'].widget.attrs.update({
            'placeholder': 'Email address'
        })


        for field in self.fields.values():
            field.help_text = ''

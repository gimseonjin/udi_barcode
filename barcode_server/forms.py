"""
This is forms module!

What i use in templates for form, in here!
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    '''
    Title : LoginForm

    This form is used in login templates

    Attributes:
        username (string) : this is marked with class form-control
        password (string) : this is marked with class form-control
    '''
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    '''
    Title : SignUpForm

    This form is used in register templates

    Attributes:
        username (string) : this is marked with class form-control
        email (string) : this is marked with class form-control
        password1 (string) : this is marked with class form-control
        password2 (string) : this is marked with class form-control

        meta (admin_user)
            fields = ('username', 'email', 'password1', 'password2')
    '''
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        """
        This is meta class for matching form data with admin user model!
        """
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UploadFileForm(forms.Form):
    '''
    Title : UploadFileForm

    This form is used in index templates to upload barcode image

    Attributes:
        file (file) : this is file field
    '''
    file = forms.FileField()

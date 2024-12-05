from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from accounts.models import CustomUser


class LoginForm(forms.Form):
    login_username = forms.CharField(max_length=100, label='Username', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': 'required'}))
    login_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'required': 'required'}))
    remember_me = forms.BooleanField(required=False, label='Remember me', widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'signin-remember-2'}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('login_username')
        password = cleaned_data.get('login_password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError('Invalid username or password.')

        return cleaned_data

class RegisterForm(forms.Form):
    register_username = forms.CharField(max_length=100, label='Username', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': 'required'}))
    register_first_name = forms.CharField(max_length=100, label='First name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name', 'required': 'required'}))
    register_last_name =  forms.CharField(max_length=100, label='Last name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name', 'required': 'required'}))
    register_email = forms.EmailField(max_length=200, label='Email Address', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address', 'required': 'required'}))
    register_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'required': 'required'}))
    register_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat password', 'required': 'required' }))
    register_policy = forms.BooleanField(required=True, label='policy', widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'register-policy-2'}))


    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("register_password1")
        password2 = cleaned_data.get("register_password2")

        if password1 != password2:
            self.add_error(None, "Passwords don't match")

        if CustomUser.objects.filter(email=cleaned_data.get("register_email")).exists():
            self.add_error('register_email', 'This email is already in use.')

        if cleaned_data.get("register_policy") != 'on':
            self.add_error(None, 'Please accept the privacy policy to proceed.')


        return cleaned_data

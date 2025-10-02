from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# Registration Form
class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=200,
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Enter your email!"})
    )
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'User Name'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password***'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password***'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# Login Form
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )

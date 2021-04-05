from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Donor


class CreateUserForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'ex.: vemba', 'class':'form-control', 'name':'username'
    }))

    firstname = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Alfredo Combo', 'class':'form-control', 'name':'firstname'
    }))

    lastname = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Nvemba', 'class':'form-control', 'name':'lastname'
    }))

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'exemplo@mail.com', 'class':'form-control', 'name':'email'
    }))

    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'placeholder': '8 ou mais digitos', 'class':'form-control', 'name':'password1', 'minlength':8
    }))

    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'placeholder': '8 ou mais digitos', 'class':'form-control', 'name':'password2', 'minlength':8
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'lastname', 'password1', 'password2']

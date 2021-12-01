from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

# Create your models here.


class CreateUserForm(UserCreationForm):
    #first_name = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
        

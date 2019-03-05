from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']



class EditProfileForm(forms.ModelForm):
    image=models.ImageField(default='user.jpeg')

    class Meta:
        model= Profile
        fields=('image',)

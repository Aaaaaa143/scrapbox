from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from scrapbox.models import Scraps,Userprofile


class RegisterationForm(UserCreationForm):

    class Meta:
        model=User
        fields=["username","email","password1","password2"]

class LoginForm(forms.Form):

    username=forms.CharField()
    password=forms.CharField()    


class ScrapForm(forms.ModelForm):

    class Meta:
        model=Scraps
        fields=["name","price","scrap_pic","category"]

class ProfileForm(forms.ModelForm):

    class Meta:
        model=Userprofile
        exclude=("user",)
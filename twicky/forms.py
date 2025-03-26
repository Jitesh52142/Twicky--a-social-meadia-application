from django import forms
from .models import Twicky
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class Twickyform(forms.ModelForm):
    class Meta:
        model = Twicky
        fields = ['text','photo']
    

class UserRegistrationsForm(UserCreationForm):
    email = forms.EmailField
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


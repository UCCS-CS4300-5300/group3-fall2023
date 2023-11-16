from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea
from .models import Feedback

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class FeedbackForm(ModelForm):
  class Meta:
    model = Feedback
    fields = ['name', 'email', 'phone', 'comments', 'gasStationAddr']
    widgets = {
      'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Name'}),
      'email' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder' : 'Email'}),
      'phone' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'Phone Number'}),
      'comments': Textarea(attrs= {'placeholder':'Leave a comment/review', 'class':'form-control', 'rows':'5'}),
      'gasStationAddr' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Gas Station Address'}),
    }
 
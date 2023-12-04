from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.models import Group
from . import models
from django.forms import ModelForm, Textarea
from .models import Feedback
from django.core.exceptions import ValidationError

from .models import GasStationOwner, GasStationListing, GasStationReview, CustomerInquiry, GasStation


class SignupForm(UserCreationForm):
  email = forms.EmailField(required=True,
                           widget=forms.EmailInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Email'
                           }))
  is_customer = forms.BooleanField(required=False,
                                   initial=False,
                                   label='Customer')
  is_gas_station_owner = forms.BooleanField(required=False,
                                            initial=False,
                                            label='Gas Station Owner')

  def clean(self):
    cleaned_data = super().clean()
    is_customer = cleaned_data.get("is_customer")
    is_gas_station_owner = cleaned_data.get("is_gas_station_owner")

    if is_customer and is_gas_station_owner:
      raise ValidationError("You can only select one checkbox.")

    if not is_customer and not is_gas_station_owner:
      raise ValidationError("Please select at least one checkbox.")

  class Meta:
    model = User
    fields = ['username', 'password1', 'password2']

    widgets = {
        'username': forms.TextInput(attrs={'class': 'form-control'}),
        'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
    }

  def save(self, commit=True):
    user = super().save(commit=False)
    user.email = self.cleaned_data['email']

    if commit:
      user.save()

      # Check if Gas Station Owner option is selected
      if self.cleaned_data['is_gas_station_owner']:
        # Create GasStationOwner instance
        gas_station_owner = GasStationOwner.objects.create(
            user=user,
            owner_name=user.username,
            contact_number='034526',
            email=user.email,
            business_address="colarado",
            emergency_contact='089754')
        # Link GasStationOwner instance to CustomUser
        user.gas_station_owner = gas_station_owner
        user.save()

    return user


# class SignupForm(UserCreationForm):
#   email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))

#   class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2']
#         widgets = {
#           'username': forms.TextInput(attrs={'class': 'form-control'}),
#           'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
#           'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
#         }
#   def save(self, commit=True):
#       user = super(SignupForm, self).save(commit=False)
#       user.email = self.cleaned_data['email']
#       if commit:
#         user.save()
#         return user


class LoginForm(forms.Form):

  username = forms.CharField(widget=forms.TextInput(
      attrs={'class': 'form-control'}))
  password = forms.CharField(widget=forms.PasswordInput(
      attrs={'class': 'form-control'}))


class GasPriceUpdateForm(forms.ModelForm):
  class Meta:
    model = models.Gas_Station
    fields = [
        'regular_gas_price', 'premium_gas_price', 'diesel_price',
        'station_name'
    ]


class FeedbackForm(ModelForm):
  class Meta:
    model = Feedback
    fields = ['name', 'email', 'phone', 'comments', 'gasStationAddr']
    widgets = {
        'name':
        forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name',
            'id': 'name'
        }),
        'email':
        forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email',
            'id': 'email'
        }),
        'phone':
        forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone Number',
            'id': 'phone'
        }),
        'comments':
        Textarea(
            attrs={
                'placeholder': 'Leave a comment/review',
                'class': 'form-control',
                'rows': '5',
                'id': 'comments'
            }),
        'gasStationAddr':
        forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Gas Station Address',
                'id': 'gasStationAddr'
            }),
    }


class GasStationForm(forms.ModelForm):
  class Meta:
    model = GasStation
    fields = '__all__'


class GasStationOwnerForm(forms.ModelForm):
  class Meta:
    model = GasStationOwner
    fields = [
        'owner_name', 'contact_number', 'email', 'business_address',
        'emergency_contact'
    ]


class GasStationOwnerForm(forms.ModelForm):
  class Meta:
    model = GasStationOwner
    fields = [
        'owner_name', 'contact_number', 'email', 'business_address',
        'emergency_contact'
    ]


class GasStationListingForm(forms.ModelForm):
  class Meta:
    model = GasStationListing

    fields = ['listing_id', 'station', 'station_owner']

    fields = ['listing_id', 'station', 'station_owner']


class GasStationReviewForm(forms.ModelForm):
  class Meta:
    model = GasStationReview
    fields = ['gas_station', 'user_name', 'rating', 'review_text']


class CustomerInquiryForm(forms.ModelForm):
  class Meta:
    model = CustomerInquiry
    fields = [
        'gas_station', 'sender_name', 'sender_email', 'message_text', 'status'
    ]

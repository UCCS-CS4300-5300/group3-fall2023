from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import GasStationOwner, GasStationListing, GasStationReview, CustomerInquiry, GasStation
class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class GasStationOwnerForm(forms.ModelForm):
    class Meta:
        model = GasStationOwner
        fields = ['owner_name', 'contact_number', 'email', 'business_address', 'emergency_contact']

class GasStationListingForm(forms.ModelForm):
    class Meta:
        model = GasStationListing
        fields = ['listing_id','station', 'station_owner']

class GasStationReviewForm(forms.ModelForm):
    class Meta:
        model = GasStationReview
        fields = ['gas_station', 'user_name', 'rating', 'review_text']

class CustomerInquiryForm(forms.ModelForm):
    class Meta:
        model = CustomerInquiry
        fields = ['gas_station', 'sender_name', 'sender_email', 'message_text', 'status']

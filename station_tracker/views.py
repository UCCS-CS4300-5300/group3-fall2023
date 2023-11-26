from .models import Feedback, AboutUs, Gas_Station
from geopy.geocoders import Nominatim
from geopy.distance import Geodesic
import folium
<<<<<<< HEAD

from .forms import UserCreationForm, LogiForm, GasStationOwnerForm, GasStationListingForm, GasStationReviewForm, CustomerInquiryForm


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import (
    UserCreationForm,
    LoginForm,
    GasStationOwnerForm,
    GasStationForm,
    GasStationListingForm,
    GasStationReviewForm,
    CustomerInquiryForm,
    GasPriceUpdateForm, 
    FeedbackForm
)


=======
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import (UserCreationForm, LoginForm, GasStationOwnerForm,
                    GasStationForm, GasStationListingForm,
                    GasStationReviewForm, CustomerInquiryForm,
                    GasPriceUpdateForm, FeedbackForm, SignupForm)
from django.contrib.auth.models import Group
>>>>>>> f509a6b0 (Users and  owners pages updated)
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import GasStationOwner, GasStationListing, GasStationReview, CustomerInquiry, GasStation
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView

# Create your views here.
#def home(request):
# return render(request, 'index.html')


# Create your views here.
# Home page
def index(request):
    return render(request, 'index.html')


# Main page
def main(request):
    # Retrieve user information
    user = request.user

    # Pass user information to the template
    context = {'user': user}
    return render(request, 'main.html', context)


# # signup page
# def user_signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)

               # form.save()
                messages.info(request, f"You are now logged in as {username}.")

                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
   # return render(request, 'login.html', {'form': form}, {'user': request.user})
        return render(request, 'login.html', {'user': request.user, 'form': form})


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Logic to assign roles based on selected checkboxes
            if form.cleaned_data['is_customer']:
                group = Group.objects.get(
                    name='Customer')  # Make sure 'Customer' group exists
                user.groups.add(group)

            if form.cleaned_data['is_gas_station_owner']:
                group = Group.objects.get(
                    name='GasStationOwner'
                )  # Ensure 'GasStationOwner' group exists
                user.groups.add(group)

            return redirect(
                'login')  
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


# logout page
def user_logout(request):

    return redirect('index')


def update_gas_prices(request):
    if request.method == 'POST':
        form = GasPriceUpdateForm(request.POST)
        if form.is_valid():
            form.save()
    Gas_Price_Update_Form = GasPriceUpdateForm()
    return render(request, 'update_gas_prices.html',
                  {"Gas_Price_Update_Form": Gas_Price_Update_Form})


<<<<<<< HEAD
  
=======
def feedback_form(request):
    return render(request, 'feedback.html')


>>>>>>> f509a6b0 (Users and  owners pages updated)
def render_feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your feedback has been submitted!")
            return redirect('feedback')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})


def map_view(request):

    geolocator = Nominatim(timeout=10, user_agent="Fuel Buddy")
    location = 'Colorado'

    stations = Gas_Station.objects.all()

    location = "Colorado springs"  # For testing, doesn't need structure so it can be any address string. zipcodes seem to be the most accurate though.

    locator = geolocator.geocode(location)  # converts addresses to coordinates
    if location == 'Colorado':
        station_map = folium.Map(
            location=[locator.latitude, locator.longitude], zoom_start=8)
    else:
        station_map = folium.Map(
            location=[locator.latitude, locator.longitude], zoom_start=13)

    folium.Marker([locator.latitude, locator.longitude]).add_to(station_map)
    folium.Circle(
        [locator.latitude, locator.longitude], radius=16090 / 2).add_to(
            station_map
        )  # distance is in meters, multiply by 1609 for conversion to miles.

    for station in stations:
        coords = (station.latitude, station.longitude)
        folium.Marker(coords).add_to(station_map)

    context = {'map': station_map._repr_html_()}

    return render(request, 'station-tracker.html', context)


def user_about(request):
    return render(request, 'about.html')

def user_fueldemand(request):
  return render(request, 'fueldemand.html')

def user_stationowner(request):
  return render(request, 'stationowner.html')

def user_payment(request):
  return render(request, 'payment.html')


# Authentication decorator
def user_authenticated(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponse("Authentication Required", status=401)
        return view_func(request, *args, **kwargs)

    return wrapper


@csrf_exempt
@login_required
def create_gas_station_owner(request):
    if request.method == 'POST':
        form = GasStationOwnerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gas station owner created successfully')
            return redirect('home')
        else:
            messages.error(request, 'Error creating gas station owner')
    else:
        form = GasStationOwnerForm()
    return render(request, 'owner_form.html', {'form': form})


@csrf_exempt
@login_required
def create_gas_station_listing(request):
    if request.method == 'POST':
        form = GasStationListingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Gas station listing created successfully')
            return redirect('gas_station_list')  # Redirect to a success page
        else:
            messages.error(request, 'Error creating gas station listing')
    else:
        form = GasStationListingForm()
    return render(request, 'listing_form.html', {'form': form})


@csrf_exempt
@login_required
def update_gas_station_listing(request, listing_id):
    listing = get_object_or_404(GasStationListing, id=listing_id)
    if request.method == 'POST':
        form = GasStationListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Gas station listing updated successfully')
            return redirect('gas_station_list')  # Redirect to a success page
        else:
            messages.error(request, 'Error updating gas station listing')
    else:
        form = GasStationListingForm(instance=listing)
    return render(request, 'listing_form.html', {'form': form})


@csrf_exempt
@login_required
def delete_gas_station_listing(request, listing_id):
    listing = get_object_or_404(GasStationListing, id=listing_id)
    if request.method == 'POST':
        listing.delete()
        messages.success(request, 'Gas station listing deleted successfully')
        return redirect('gas_station_list')  # Redirect to a success page
    return render(request, 'confirm_delete.html', {'listing': listing})


# Create gas station review
@csrf_exempt
@login_required
def create_gas_station_review(request):
    if request.method == 'POST':
        form = GasStationReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Gas station review created successfully')
            return redirect('/')  # Redirect to a success page
        else:
            messages.error(request, 'Error creating gas station review')
    else:
        form = GasStationReviewForm()
    return render(request, 'review_form.html', {'form': form})


# Update gas station review
@csrf_exempt
@login_required
def update_gas_station_review(request, review_id):
    review = get_object_or_404(GasStationReview, id=review_id)
    if request.method == 'POST':
        form = GasStationReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Gas station review updated successfully')
            return redirect('/')  # Redirect to a success page
        else:
            messages.error(request, 'Error updating gas station review')
    else:
        form = GasStationReviewForm(instance=review)
    return render(request, 'review_form.html', {'form': form})


# Delete gas station review
@csrf_exempt
@login_required
def delete_gas_station_review(request, review_id):
    review = get_object_or_404(GasStationReview, id=review_id)
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Gas station review deleted successfully')
        return redirect('/')  # Redirect to a success page
    return render(request, 'confirm_delete_review.html', {'review': review})


# Create customer inquiry


@csrf_exempt
@login_required
def update_gas_station_owner(request, owner_id):
    owner = get_object_or_404(GasStationOwner, id=owner_id)
    if request.method == 'POST':
        form = GasStationOwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gas station owner updated successfully')
            return redirect('/')  # Redirect to a success page
        else:
            messages.error(request, 'Error updating gas station owner')
    else:
        form = GasStationOwnerForm(instance=owner)
    return render(request, 'owner_form.html', {'form': form})


@csrf_exempt
@login_required
def delete_gas_station_owner(request, owner_id):
    owner = get_object_or_404(GasStationOwner, id=owner_id)
    if request.method == 'POST':
        owner.delete()
        messages.success(request, 'Gas station owner deleted successfully')
        return redirect('/')  # Redirect to a success page
    return render(request, 'confirm_delete.html', {'owner': owner})


@csrf_exempt
@login_required
def create_customer_inquiry(request):
    if request.method == 'POST':
        form = CustomerInquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer inquiry created successfully')
            return redirect('/')  # Redirect to a success page
        else:
            messages.error(request, 'Error creating customer inquiry')
    else:
        form = CustomerInquiryForm()
    return render(request, 'inquiry_form.html', {'form': form})


@csrf_exempt
@login_required
def update_customer_inquiry(request, inquiry_id):
    inquiry = get_object_or_404(CustomerInquiry, id=inquiry_id)
    if request.method == 'POST':
        form = CustomerInquiryForm(request.POST, instance=inquiry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer inquiry updated successfully')
            return redirect('/')  # Redirect to a success page
        else:
            messages.error(request, 'Error updating customer inquiry')
    else:
        form = CustomerInquiryForm(instance=inquiry)
    return render(request, 'inquiry_form.html', {'form': form})


@csrf_exempt
@login_required
def delete_customer_inquiry(request, inquiry_id):
    inquiry = get_object_or_404(CustomerInquiry, id=inquiry_id)
    if request.method == 'POST':
        inquiry.delete()
        messages.success(request, 'Customer inquiry deleted successfully')
        return redirect('/')  # Redirect to a success page
    return render(request, 'confirm_delete.html', {'inquiry': inquiry})


# def gas_station_list(request):
#     gas_stations = GasStationListing.objects.all()
#     return render(request, 'gas_station_list.html', {'gas_stations': gas_stations})
class GasStationListView(ListView):

    model = GasStationListing
    template_name = 'gas_station_list.html'
    context_object_name = 'gas_stations'


def gas_station_form(request, action, gas_station=None):
    form = GasStationForm(
        instance=gas_station) if gas_station else GasStationForm()

    context = {
        'form': form,
        'action': action,
        'gas_station': gas_station,
    }

    return render(request, 'gas_station_form.html', context)


def create_gas_stations(request):
    if request.method == 'POST':
        form = GasStationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('ga-stations/')
        else:
            # If the form is not valid, re-render the form with errors
            return render(request, 'gas_station_form.html', {'form': form})
    else:
        # For GET request, render an empty form
        form = GasStationForm()
        return render(request, 'gas_station_form.html', {'form': form})


def update_gas_station(request, gas_station_id):
    gas_station = get_object_or_404(GasStation, id=gas_station_id)
    if request.method == 'POST':
        form = GasStationForm(request.POST, instance=gas_station)
        if form.is_valid():
            form.save()
            # Redirect or render success page
            return redirect('gas-stations/')
    else:
        return gas_station_form(request, 'update', gas_station)


def delete_gas_station(request, gas_station_id):
    gas_station = get_object_or_404(GasStation, id=gas_station_id)
    if request.method == 'POST':
        gas_station.delete()
        # Redirect or render success page
        return redirect('gas_stations')
    else:
        return gas_station_form(request, 'delete', gas_station)


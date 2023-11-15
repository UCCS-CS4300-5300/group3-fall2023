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
)

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


# signup page
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


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
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


# logout page
def user_logout(request):
    logout(request)
    return redirect('login')


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

            return redirect(
                'ga-stations/'
            )  
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

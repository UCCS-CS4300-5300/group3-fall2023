from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Feedback, AboutUs, Gas_Station
from django.http import HttpResponse
from geopy.geocoders import Nominatim
from geopy.distance import Geodesic
from .forms import FeedbackForm
import folium




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
               # form.save()
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
   # return render(request, 'login.html', {'form': form}, {'user': request.user})
        return render(request, 'login.html', {'user': request.user, 'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('index')


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
    
    stations =  Gas_Station.objects.all()
    
    location = "Colorado springs" # For testing, doesn't need structure so it can be any address string. zipcodes seem to be the most accurate though.

    locator = geolocator.geocode(location) # converts addresses to coordinates
    if location is 'Colorado':
        station_map = folium.Map(location=[locator.latitude, locator.longitude], zoom_start=8)
    else:
        station_map = folium.Map(location=[locator.latitude, locator.longitude], zoom_start=13)

    
    folium.Marker([locator.latitude, locator.longitude]).add_to(station_map)
    folium.Circle([locator.latitude, locator.longitude], radius=16090/2).add_to(station_map) # distance is in meters, multiply by 1609 for conversion to miles. 

    for station in stations:
        coords = (station.latitude, station.longitude)
        folium.Marker(coords).add_to(station_map)

    context = {'map': station_map._repr_html_()}
    return render(request, 'station-tracker.html', context)

def user_about(request):
  return render(request, 'about.html')

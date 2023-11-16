from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm, FeedbackForm
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


from .models import Feedback, Gas_Station
from geopy.geocoders import Nominatim
from geopy.distance import Geodesic
import folium

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

    def gas_station_view(request):
    stations = Gas_Station.objects.all()

    serialized_data = [

        {
            'id': station.id,
            'name': station.name,
            'location': station.location,
            'additions': station.additions,
        }
        for station in stations
    ]
    response_data = {
        'list' : serialized_data
    }

    return render(request, 'displaymodel.html', {'data': response_data})
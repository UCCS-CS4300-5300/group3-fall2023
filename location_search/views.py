from . import models
from django.shortcuts import render
import requests
from django.views.generic.edit import UpdateView,CreateView
from .forms import SearchForm
from django.shortcuts import render, redirect
from .models import Search
from django.shortcuts import render, get_object_or_404, get_list_or_404
from geopy.geocoders import Nominatim
from geopy.distance import Geodesic
import folium
from folium import IFrame
from .forms import SearchForm
from django.http import HttpResponse
from station_tracker.models import Gas_Station
import os






def submit(request):
    if request.method == 'POST':
        # This is where you handle the POST request and save data to your database
        search = request.POST.get('location', '')
        range = request.POST.get('range', '')
        fuelType = request.POST.get('gasType', '')
        searchPref = request.POST.get('preferenceSelect', '')

        search = Search(location=search,range = range, fuelType = fuelType, searchPref = searchPref)
        search.save()

        my_secret = os.environ['api_key']
        
        locationInfo = geocode(search,my_secret)

        lat_lng = locationInfo['results'][0]['geometry']['location']
        print(lat_lng)


        
        gas_station_database(request, lat_lng, 7000,my_secret)
        request.session['map_context'] = map_viewSubmit(request, search, range)

        
        
    return redirect("searchPage")    

def searchPage(request):
    

    map_context = request.session.get('map_context', {})

    my_secret = os.environ['api_key']

    map_context['GOOGLE_API_KEY'] = my_secret

    return render(request,'stuff.html', map_context)

#############################################
#Google maps API functions
def my_view(request):
    context = {'GOOGLE_API_KEY': os.environ['api_key']}
    return render(request, 'stuff.html', context)


def geocode(address, api_key):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": api_key,
    }
    response = requests.get(base_url, params=params)
    return response.json()
    
def nearby_gas_search(location,radius, api_key):
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    location = f"{location['lat']},{location['lng']}"
    params = {
        "location": location,
        "radius": radius,
        "type": "gas_station",
        "key": api_key,
    }
    response = requests.get(base_url, params=params)
    return response.json()


    

    

def gas_station_database(request, location, radius, api_key):
    # Get data from the Google Places API
    data = nearby_gas_search(location, radius, api_key)
    #print(data)

    gas_secret = os.environ['gas_key']
    

    # Iterate over each result in the data
    for result in data['results']:
        # Create a new GasStation object

        
        gas_station = Gas_Station(
            station_name=result['name'],
            address=result['vicinity'],
            latitude=result['geometry']['location']['lat'],
            longitude=result['geometry']['location']['lng'],
            regular_gas_price = 0,
            premium_gas_price = 0,
            diesel_price = 0
        )

        #print(gas_station)

        # Save the GasStation object to the database
        gas_station.save()


    
def map_view(request):
    
    geolocator = Nominatim(timeout=10, user_agent="Fuel Buddy")
    location = 'Colorado'
    
    stations =  Gas_Station.objects.all()
    
    location = "Colorado springs" # For testing, doesn't need structure so it can be any address string. zipcodes seem to be the most accurate though.

    locator = geolocator.geocode(location) # converts addresses to coordinates
    if location == 'Colorado':
        station_map = folium.Map(location=[locator.latitude, locator.longitude], zoom_start=8)
    else:
        station_map = folium.Map(location=[locator.latitude, locator.longitude], zoom_start=13)

    
    folium.Marker([locator.latitude, locator.longitude], icon = folium.Icon(color='red')).add_to(station_map)
    folium.Circle([locator.latitude, locator.longitude], radius=16090/2).add_to(station_map) # distance is in meters, multiply by 1609 for conversion to miles. 

    for station in stations:
        coords = (station.latitude, station.longitude)
        folium.Marker(coords).add_to(station_map)

    context = {'map': station_map._repr_html_()}

    my_secret = os.environ['api_key']

    context['GOOGLE_API_KEY'] = my_secret
    
    return render(request, 'stuff.html', context)

def map_viewSubmit(request, search, userRange):

    geolocator = Nominatim(timeout=10, user_agent="Fuel Buddy")
    location = 'Colorado'

    stations =  Gas_Station.objects.all()

    location = search # For testing, doesn't need structure so it can be any address string. zipcodes seem to be the most accurate though.

    locator = geolocator.geocode(location) # converts addresses to coordinates
    if location == 'Colorado':
        station_map = folium.Map(location=[locator.latitude, locator.longitude], zoom_start=8)
    else:
        station_map = folium.Map(location=[locator.latitude, locator.longitude], zoom_start=13)

    #Convert user string to int, and convert it to meters
    range = convToRange(userRange) * 1609


    folium.Marker([locator.latitude, locator.longitude], icon = folium.Icon(color='red')).add_to(station_map)
    folium.Circle([locator.latitude, locator.longitude], radius=range/2).add_to(station_map)
                  # distance is in meters, multiply by 1609 for conversion to miles. 

    for station in stations:
        
        coords = (station.latitude, station.longitude)
        #Get google maps URL to the gas station
        #google_maps_link = f"<a href = http://maps.google.com/?q={station.address.replace(' ', '+')}>Maps to location</a>"
        
        
        
        

        #Mark each gas station with marker and popup with station name and link to  google maps
        folium.Marker(coords, tooltip = station.station_name + ": "+ station.address, popup = folium.Popup(f"<a href = http://maps.google.com/?q={station.address.replace(' ', '+')}>Directions</a>")).add_to(station_map)

    context = {'map': station_map._repr_html_()}
    return context

def convToRange(userRange):
    if userRange == '5 Miles':
        return 5
    elif userRange == '10 Miles':
        return 10
    elif userRange == '20 Miles':
        return 20
    else:
        return 10



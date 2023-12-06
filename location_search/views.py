from . import models
from django.shortcuts import render
import requests
from django.views.generic.edit import UpdateView,CreateView
from .forms import SearchForm
from django.shortcuts import render, redirect
from .models import Gas_Station, Search
from django.shortcuts import render, get_object_or_404, get_list_or_404
from geopy.geocoders import Nominatim
from geopy.distance import Geodesic
import folium
from django.http import HttpResponse



def searchPage(request):
    return render(request,'stuff.html')


def submit(request):
    if request.method == 'POST':
        # This is where you handle the POST request and save data to your database
        search = request.POST.get('location', '')
        range = request.POST.get('range', '')
        fuelType = request.POST.get('gasType', '')
        searchPref = request.POST.get('preferenceSelect', '')

        search = Search(location=search,range = range, fuelType = fuelType, searchPref = searchPref)
        search.save()

        map_context = map_viewSubmit(request)

        return render(request, 'stuff.html', map_context)
        
    return render(request, 'stuff.html')
    

    
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

    
    folium.Marker([locator.latitude, locator.longitude]).add_to(station_map)
    folium.Circle([locator.latitude, locator.longitude], radius=16090/2).add_to(station_map) # distance is in meters, multiply by 1609 for conversion to miles. 

    for station in stations:
        coords = (station.latitude, station.longitude)
        folium.Marker(coords).add_to(station_map)

    context = {'map': station_map._repr_html_()}
    return render(request, 'stuff.html', context)

def map_viewSubmit(request):

    geolocator = Nominatim(timeout=10, user_agent="Fuel Buddy")
    location = 'Colorado'

    stations =  Gas_Station.objects.all()

    location = "Colorado springs" # For testing, doesn't need structure so it can be any address string. zipcodes seem to be the most accurate though.

    locator = geolocator.geocode(location) # converts addresses to coordinates
    if location == 'Colorado':
        station_map = folium.Map(location=[locator.latitude, locator.longitude], zoom_start=8)
    else:
        station_map = folium.Map(location=[locator.latitude, locator.longitude], zoom_start=13)


    folium.Marker([locator.latitude, locator.longitude]).add_to(station_map)
    folium.Circle([locator.latitude, locator.longitude], radius=16090/2).add_to(station_map) # distance is in meters, multiply by 1609 for conversion to miles. 

    for station in stations:
        coords = (station.latitude, station.longitude)
        folium.Marker(coords).add_to(station_map)

    context = {'map': station_map._repr_html_()}
    return context
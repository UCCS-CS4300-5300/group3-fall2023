
from django.urls import path
from .views import GasStationListView
from . import views
from django.urls import path, include

urlpatterns = [
   path('', views.index, name='home'),
   

   path('login/', views.user_login, name='login'),
   path('signup/', views.user_signup, name='signup'),
   path('logout/', views.user_logout, name='logout'),
   path('update_gas_prices/', views.update_gas_prices, name="update_gas_prices"),
   path('location_search/', include('location_search.urls')),
   path('feedback/', views.render_feedback_form, name="feedback"),
   path('station-tracker/', views.map_view, name="station-tracker"),
   path('about/', views.user_about, name="about"),
   path('fueldemand/', views.user_fueldemand, name="fueldemand"),
   path('stationowner/', views.user_stationowner, name="stationowner"),
   path('payment/', views.user_payment, name="payment"),




# 
#     # path('', home,name="home"),
#     path('', views.index, name='home'),
#     path('login/', views.user_login, name='login'),
#     path('signup/', views.user_signup, name='signup'),
#     path('logout/', views.user_logout, name='logout'),
#     # Gas Station Owner URLs
    path('create-owner/',
         views.create_gas_station_owner,
         name='create_gas_station_owner'),
    path('update-owner/<int:owner_id>/',
         views.update_gas_station_owner,
         name='update_gas_station_owner'),
    path('delete-owner/<int:owner_id>/',
         views.delete_gas_station_owner,
         name='delete_gas_station_owner'),



    # Gas Station Listing URLs
    path('create-listing/',
         views.create_gas_station_listing,
         name='create_gas_station_listing'),
    path('update-listing/<int:listing_id>/',
         views.update_gas_station_listing,
         name='update_gas_station_listing'),
    path('delete-listing/<int:listing_id>/',
         views.delete_gas_station_listing,
         name='delete_gas_station_listing'),

    # Gas Station Review URLs
    path('create-review/',
         views.create_gas_station_review,
         name='create_gas_station_review'),
    path('update-review/<int:review_id>/',
         views.update_gas_station_review,
         name='update_gas_station_review'),
    path('delete-review/<int:review_id>/',
         views.delete_gas_station_review,
         name='delete_gas_station_review'),

    # Customer Inquiry URLs
    path('create-inquiry/',
         views.create_customer_inquiry,
         name='create_customer_inquiry'),
    path('update-inquiry/<int:inquiry_id>/',
         views.update_customer_inquiry,
         name='update_customer_inquiry'),
    path('delete-inquiry/<int:inquiry_id>/',
         views.delete_customer_inquiry,
         name='delete_customer_inquiry'),
    # path('gas-stations/', views.gas_station_list, name='gas_station_list'),
    path('gas-stations/',
         GasStationListView.as_view(),
         name='gas_station_list'),
# gas station urls
    path('create-gas-station/', views.create_gas_stations, name='create_gas_stations'),
      path('<int:gas_station_id>/update/', views.update_gas_station, name='update_gas_station'),

      path('delete/<int:gas_station_id>', views.delete_gas_station, name='delete_gas_station'),

  ]
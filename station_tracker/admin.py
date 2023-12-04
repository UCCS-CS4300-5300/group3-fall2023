from django.contrib import admin
from .models import GasStationOwner, GasStationListing, GasStationReview, CustomerInquiry, GasStation, Gas_Station, Feedback
#from .models import gas_station_tracker

admin.site.register(Gas_Station)


@admin.register(GasStation)
class GasStationAdmin(admin.ModelAdmin):
  list_display = ('name', 'location', 'latitude', 'longitude', 'owner')


@admin.register(GasStationOwner)
class GasStationOwnerAdmin(admin.ModelAdmin):
  list_display = ('owner_name', 'contact_number', 'email', 'business_address')


@admin.register(GasStationListing)
class GasStationListingAdmin(admin.ModelAdmin):
  list_display = ('listing_id', 'station', 'station_owner')


@admin.register(GasStationReview)
class GasStationReviewAdmin(admin.ModelAdmin):
  list_display = ('gas_station', 'user_name', 'rating', 'review_text')


@admin.register(CustomerInquiry)
class CustomerInquiryAdmin(admin.ModelAdmin):
  list_display = ('gas_station', 'sender_name', 'sender_email', 'timestamp',
                  'status')
  list_filter = ('status', )  # Enable filtering by status in the admin panel

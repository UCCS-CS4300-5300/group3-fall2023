from django.db import models


class GasStation(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    owner = models.ForeignKey('GasStationOwner', on_delete=models.CASCADE)
    services_offered = models.TextField()
    amenities = models.TextField()

    def __str__(self):
        return self.name

# Gas Station Owner Profile Model
class GasStationOwner(models.Model):
    owner_id= models.AutoField(primary_key=True,default=0)
    owner_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    business_address = models.CharField(max_length=255)
    emergency_contact = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
      return self.owner_name

# Gas Station Listing Model
class GasStationListing(models.Model):
    listing_id = models.AutoField(primary_key=True)
    station =models.ForeignKey(GasStation, on_delete=models.CASCADE)  
    station_owner = models.ForeignKey(GasStationOwner, on_delete=models.CASCADE)

def __str__(self):
  return  f"{self.station.name} Listing"

# Review Model
class GasStationReview(models.Model):
    review_id = models.AutoField(primary_key=True)
    gas_station = models.ForeignKey(GasStationListing, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)
    review_text = models.TextField()

# Message Model for Customer Inquiries

class CustomerInquiry(models.Model):
    inquiry_id = models.AutoField(primary_key=True)
    gas_station = models.ForeignKey(GasStationListing, on_delete=models.CASCADE)
    sender_name = models.CharField(max_length=100)
    sender_email = models.EmailField()
    message_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ('Pending', 'Pending'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='Pending')

    def __str__(self):
        return f"Inquiry from {self.sender_name} about {self.gas_station}"

    class Meta:
        ordering = ['-timestamp']

from django.db import models


# Create your models here.

class Gas_Station(models.Model):
  station_name = models.CharField(max_length=200)
  latitude = models.FloatField()
  longitude = models.FloatField()
  regular_gas_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
  premium_gas_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
  diesel_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
  
  def __str__(self):
    return self.station_name
  
class Feedback(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField()
  phone = models.IntegerField()
  comments = models.TextField()
  gasStationAddr = models.CharField(max_length=200)

  def __str__(self):
    return self.name
  
<<<<<<< HEAD
      
        # Model for the About Us page
class AboutUs(models.Model):
        # Fields for the About Us page
        title = models.CharField(max_length=200)
        content = models.TextField()
        image = models.ImageField(upload_to='about_us_images/')
        # Add any other fields you need for the About Us page

    

=======
def __str__(self):
        return self.name

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
       
>>>>>>> 173a3f15 (created the owner , gas station, reviews ,and  inquiry  functionality thst spplies crud)

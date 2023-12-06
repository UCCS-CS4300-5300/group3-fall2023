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
  
      
        # Model for the About Us page
class AboutUs(models.Model):
        # Fields for the About Us page
        title = models.CharField(max_length=200)
        content = models.TextField()
        image = models.ImageField(upload_to='about_us_images/')
        # Add any other fields you need for the About Us page

    
class UserRewards(models.Model):
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  points = models.IntegerField(default=0)

class RewardTypes(models.Model):
  RewardType = models.CharField(max_length=200)
  RewardPointsAmount = models.IntegerField()
  RewardDescription = models.TextField()
  
class EarnRewards(models.Model):
  GasStation = models.ForeignKey(Gas_Station, on_delete=models.CASCADE)
  MoneySpent = models.IntegerField(default=0)
  RewardType = models.ForeignKey(RewardTypes, on_delete=models.CASCADE)


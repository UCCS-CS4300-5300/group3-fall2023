from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
#Note: PhoneNumberField is a custom module for Django installed via pip

class Feedback(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField()
  phone = PhoneNumberField(null=False, blank=False, unique=True)
  message = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  #todo: implement pointer to company
  
  def __str__(self):
    return self.name

class Address(models.Model):
    street = models.CharField(verbose_name="Street Name", max_length=50)
    num = models.CharField(verbose_name="Street Number", max_length=50)
    city = models.CharField(verbose_name="City", max_length=50)
    state = models.CharField(verbose_name="State", max_length=50)
    zip_code = models.CharField(verbose_name="Zip Code", max_length=50)    
    country = models.CharField(verbose_name="Country", max_length=50)
    #add latitude, longitude?

    def __str__(self):
        return '%s %s %s %s %s %s'%(self.street, self.num, self.city, self.state, self.zip_code, self.country)

class Addition(models.Model):
    air_pump = models.CharField(verbose_name="Air Pump", max_length=50)
    electric_charging = models.CharField(verbose_name="E-charge", max_length=50)
    resturants = models.CharField(verbose_name="Resturants", max_length=50)

    def __str__(self):
        return '%s %s %s'%(self.air_pump, self. electric_charging, self.resturants)

class Gas_Station(models.Model):
    name = models.CharField(max_length=50)
    location = models.ForeignKey(Address, verbose_name="Location",  default="Unknown", on_delete=models.CASCADE)
    additions = models.ForeignKey(Addition, verbose_name="Additions", default="None", on_delete=models.CASCADE)
    #phone_number
    #hours

    def __str__(self):
        return '%s %s %s'%(self.name, self.location, self.additions)


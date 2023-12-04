from django.contrib import admin
from .models import Gas_Station
# Register your models here.
from .models import Search
#Search information
admin.site.register(Search)



admin.site.register(Gas_Station)

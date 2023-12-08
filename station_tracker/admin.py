
# Register your models here.
from django.contrib import admin
from .models import Gas_Station, Feedback, UserRewards, RewardTypes, EarnRewards
#from .models import gas_station_tracker

admin.site.register(Gas_Station)
admin.site.register(UserRewards)
admin.site.register(RewardTypes)
admin.site.register(EarnRewards)
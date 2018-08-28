from django.contrib import admin
from .models import Car, Owner, Profile
# Register your models here.

class CarModelAdmin(admin.ModelAdmin):
    list_display = ['vin_number','car_model','car_type','made', 'owner']
    list_filter = ['car_model']
    search_fields = ['car_model','owner__name','owner__dob', 'owner__id']
    raw_id_fields = ['owner']
    class Meta:
        model = Car


admin.site.register(Car,CarModelAdmin)
admin.site.register(Owner)
admin.site.register(Profile)
# admin.site.register(CarModelAdmin)

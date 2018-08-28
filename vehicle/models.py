from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=30, verbose_name="Full Name")
    dob = models.DateField(verbose_name="Date of Birth",blank=True,null=True,
                           default=datetime.date(year=datetime.date.today().year-18,month=6,day=15))
    sex = models.CharField(max_length=2,choices=[('m',"Male"),("f","Female")],default="m")
    address = models.TextField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name


CAR_MODEL=[
    ('ho','Honda'), ('to','Toyota'), ('fo','Force'), ('su','Suzuki')
]
CAR_TYPE_CHOICE = (
    ('se','Sedan'), ('sp',"Sport"), ('va','Van'), ('tr','Truck')
)
YEAR_MADE =[(str(x),x) for x in reversed(range(timezone.now().year-25,timezone.now().year+1))]
class Car(models.Model):
    vin_number = models.CharField(max_length=18, blank=False,null=True)
    car_model = models.CharField(max_length=20, blank=False, null=False, choices=CAR_MODEL, default='ho')
    made = models.CharField(max_length=10,choices=YEAR_MADE, default=timezone.now().year)
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE, null=True, related_name="vehicle_car")
    car_type = models.CharField(max_length=30, blank=True, choices=CAR_TYPE_CHOICE, default='se')
    date_add = models.DateField(auto_now=False, default=timezone.now())

    def __str__(self):
        return str(self.vin_number + " " + self.car_model)

class Profile(models.Model):
    owner = models.OneToOneField(Owner, on_delete=models.DO_NOTHING, null=True)
    email = models.EmailField(max_length=200, blank=True,null=True)
    phone = models.CharField(max_length=15,null=True,blank=True)
    date_join = models.DateField(auto_now=False,default=timezone.now())

    def __str__(self):
        return self.owner.name



from django.db import models
from django.utils import timezone

# Create your models here.
from vehicle.models import Car
from vehicle.models import Profile
POLICY_TYPE =[
    ('homenauto','Home & Auto Insurance'),
    ('auto','Auto Insurance'),
    ('personal','Personal Insurance'),
    ('farm','Farm Insurance'),
    ('life','Life Insurance'),
    ('health','Health Insurance'),
    ('techservice','Technology Services Insurance'),
    ('recreationalvehicle','Recreational Vehicle Insurance'),
    ('finacial','Financial Services'),
]
POLICY_STATUS=[
    ('active','Active'),
    ('inactive','Inactive'),
    ('cancel','Cancel'),
    ('pending','Pending')
]
class Policy(models.Model):
    policy_number = models.CharField(max_length=15, null=False, blank=False)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="insurance_policies", verbose_name='Car Vin number')
    date_apply = models.DateField(null=False, blank=False, default=timezone.datetime.today())
    date_add = models.DateField(null=True, blank=True, auto_now_add=timezone.now())
    user_add = models.OneToOneField(Profile,
                                    on_delete=models.DO_NOTHING, related_name='user_policies', null=True)
    type= models.CharField(max_length=12,choices= POLICY_TYPE, default='personal')
    status = models.CharField(max_length=10,choices=POLICY_STATUS, default='active')

    def __str__(self):
        return self.policy_number
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from account.models import *



class Farmer(models.Model):
    farmer = models.ForeignKey(
            Account, 
            on_delete=models.SET_NULL, 
            null=True, 
            blank=True
    )
    first_name = models.CharField(max_length=100, default="-")
    last_name = models.CharField(max_length=100, default="-")
    phone = models.CharField(max_length=15, default="-")
    email = models.EmailField(max_length = 254, default="-")
    street = models.CharField(max_length=100, default="-")
    house_num = models.CharField(max_length=100, default="-")
    postal_code = models.CharField(max_length=100, default="-")
    postal_city = models.CharField(max_length=100, default="-")

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return self.last_name



class Farm(models.Model):
    farm_name = models.CharField(max_length=100, default="-")
    farm_id_num = models.CharField(max_length=100, default="-")
    farmers = models.ForeignKey(Farmer, on_delete=models.SET_NULL, null=True, blank=True)

    FARM_TYPES = (
        ('1', 'Uprawy polowe'),
        ('2', 'Uprawy ogrodnicze'),
        ('3', 'Uprawy trwałe'),
        ('4', 'Krowy mleczne'),
        ('5', 'Zwierzęta trawożerne'),
        ('6', 'Trzoda chlewna'),
        ('7', 'Drób'),
        ('8', 'Mieszane'),

    )
    farm_type = models.CharField(max_length=1, choices=FARM_TYPES, blank=True, null=True)


    class Meta:
        ordering = ['farm_name']

    def __str__(self):
        return self.farm_name













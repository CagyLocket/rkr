from django.db import models

# Create your models here.
from account.models import Account



# Rodzaje gospodarstw rolnych

# Gospodsrstwa rolne w podziale na typy rolnicze wg 
#Wspólnotowej Typologii  Gospodarstw Rolnych (TF8):
# https://fadn.pl/publikacje/wyniki-w-skrocie/ws-w-skrocie-w-typach/

# Uprawy polowe, Uprawy ogrodnicze, Uprawy trwałe, Krowy mleczne, 
# Zwierzęta trawożerne, Trzoda chlewna, Drób, Mieszane



# class Farmer(models.Model):
#     first_name = models.CharField(max_length=30, blank=True, null=True)
#     last_name = models.CharField(max_length=30, blank=True, null=True)
#     # users = models.ForeignKey(Account, on_delete=models.CASCADE)
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     email = models.EmailField(max_length = 254, blank=True, null=True )
#     street = models.CharField(max_length=100, blank=True, null=True)
#     house_num = models.CharField(max_length=100, blank=True, null=True)
#     postal_code = models.CharField(max_length=100, blank=True, null=True)
#     postal_city = models.CharField(max_length=100, blank=True, null=True)

#     class Meta:
#         ordering = ['last_name']

#     def __str__(self):
#         return self.last_name


# class Farm(models.Model):
#     farm_name = models.CharField(max_length=100, blank=True, null=True)
#     farm_id_num = models.CharField(max_length=100, blank=True, null=True)
#     farmers = models.ForeignKey(Farmer, on_delete=models.CASCADE)

#     FARM_TYPES = (
#         ('1', 'Uprawy polowe'),
#         ('2', 'Uprawy ogrodnicze'),
#         ('3', 'Uprawy trwałe'),
#         ('4', 'Krowy mleczne'),
#         ('5', 'Zwierzęta trawożerne'),
#         ('6', 'Trzoda chlewna'),
#         ('7', 'Drób'),
#         ('8', 'Mieszane'),

#     )
#     farm_type = models.CharField(max_length=1, choices=FARM_TYPES, blank=True, null=True)


#     class Meta:
#         ordering = ['farm_name']

#     def __str__(self):
#         return self.farm_name


# class FarmIdentificationData(models.Model):
#     farmer_name = models.CharField(max_length=100)
#     farmer_surname = models.CharField(max_length=100)

#     voivodeship = models.CharField(max_length=100)
#     district = models.CharField(max_length=100)
#     commune = models.CharField(max_length=100)
#     street = models.CharField(max_length=100)
#     house_num = models.CharField(max_length=100)
#     postal_code = models.CharField(max_length=100)
#     postal_city = models.CharField(max_length=100)
#     residance_city = models.CharField(max_length=100)
#     farm_id_num = models.CharField(max_length=100)
#     farm_phone = models.CharField(max_length=100)
#     farm_email = models.CharField(max_length=100)



#     publications = models.ManyToManyField(Farmer)

#     class Meta:
#         ordering = ['headline']

#     def __str__(self):
#         return self.headline


# class Company(models.Model):
#     company_name = models.CharField(max_length=100)
#     vat_num = models.CharField(max_length=100)
#     # vat_form = models.CharField(max_length=100) [ 0 ] ryczałt, [ 1 ] zasady ogólne
#     nip = models.CharField(max_length=100)
#     regon = models.CharField(max_length=100)
#     registered_street = models.CharField(max_length=100)
#     registered_house_num = models.CharField(max_length=100)
#     registered_postal_code = models.CharField(max_length=100)
#     registered_postal_city = models.CharField(max_length=100)
#     bank_name = models.CharField(max_length=100)
#     bank_account = models.CharField(max_length=100)

#     publications = models.ManyToManyField(Publication)

#     class Meta:
#         ordering = ['company_name']

#     def __str__(self):
#         return self.company_name
















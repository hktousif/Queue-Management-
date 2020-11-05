from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    Type = (('Hospital', 'Hospital'),
            ('Service', 'Service'),
            ('Salon', 'Salon')
            )
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    companyName = models.CharField(max_length=150)
    phoneNumber = models.CharField(max_length=13)
    workingHour = models.CharField(max_length=250)
    serviceType = models.CharField(choices=Type, max_length=25)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    zipCode = models.IntegerField()
    mapLink = models.CharField(max_length=250)
    others = models.CharField(max_length=250, blank=True, null=True)
    timeStamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class TokenNoHandler(models.Model):
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    tokenNo = models.IntegerField(default=0)
    timeStamp = models.DateField(auto_now=True)

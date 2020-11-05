from django.contrib.auth.models import User
from django.db import models
from django.db.models.functions import datetime

from clients.models import Company


class Appointments(models.Model):
    STATUS = (('Completed', 'Completed'),
              ('Pending', 'Pending'),
              ('InQueue', 'In Queue'),
              )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    tokenNo = models.IntegerField()
    phone = models.CharField(max_length=13)
    status = models.CharField(choices=STATUS, max_length=30)
    other = models.CharField(max_length=150, blank=True, null=True)
    timeStamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     prev = Appointments.objects.filter(company=self.company).order_by('id').last()
    #     if prev:
    #         if datetime.datetime.date(prev.timeStamp) != datetime.datetime.now().date():
    #             self.tokenNo = 1
    #         self.tokenNo = int(prev.tokenNo) + 1
    #     else:
    #         self.tokenNo = 1
    #     super().save(*args, **kwargs)




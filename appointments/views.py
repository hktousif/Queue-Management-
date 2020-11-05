from django.shortcuts import render
from rest_framework import viewsets

from appointments.models import Appointments
from appointments.serializers import AppointmentSer


class AppointmentView(viewsets.ModelViewSet):
    serializer_class = AppointmentSer
    queryset = Appointments.objects.all()

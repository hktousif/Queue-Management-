from django.db import transaction
from rest_framework.serializers import ModelSerializer

from clients.models import TokenNoHandler
from .models import *


class AppointmentSer(ModelSerializer):
    class Meta:
        model = Appointments
        fields = '__all__'
        read_only_fields = ['tokenNo']
        # depth = 1

    def create(self, validated_data):
        with transaction.atomic():
            prev = TokenNoHandler.objects.select_for_update().get(company=validated_data['company'])
            if prev.timeStamp != datetime.datetime.now().date():
                validated_data['tokenNo'] = 1
                prev.tokenNo = 0
                prev.save()
            else:
                validated_data['tokenNo'] = prev.tokenNo + 1
                prev.save(tokenNo=validated_data['tokenNo'])
        return Appointments.objects.create(**validated_data)

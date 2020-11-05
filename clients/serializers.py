from rest_framework.serializers import ModelSerializer

from .models import *


class CompanySer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ['owner']
        # depth = 1

    def create(self, validated_data):
        company = Company.objects.create(**validated_data)
        TokenNoHandler.objects.get_or_create(company=company)
        return company

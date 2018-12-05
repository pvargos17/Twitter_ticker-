from rest_framework import serializers
from .models import Company
from .company_name import mydict


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("company_name","ticker_symbol")


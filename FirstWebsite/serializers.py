from rest_framework import serializers
from .models import Merchant, DealProvider, Deals


class MerchantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Merchant
        fields = '__all__'


class DealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deals
        fields = ('dealPro', 'dealName', 'dealSummary', 'dealImg')


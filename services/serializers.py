from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):

    def validate_price(self, price):
        if price <= 0:
            raise serializers.ValidationError("O preço deve ser maior que zero")
        return price

    def validate_duration(self, duration):
        return duration
            
    class Meta:
        model = Service
        fields = ['id', 'name', 'description',  'price', 'duration', 'status']
        read_only_fields = ['id', 'status']
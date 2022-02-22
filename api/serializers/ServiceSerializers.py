from rest_framework import serializers
from api.models import Service

class ServiceSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Service
        fields = (
           'id', 'name', 'image', 'detail', 'price', "created_at", "updated_at"
        )
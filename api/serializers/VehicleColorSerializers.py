from rest_framework import serializers
from api.models import VehicleColor

class VehicleColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleColor
        fields = (
           'id', 'name', 'color', "created_at", "updated_at"
        )
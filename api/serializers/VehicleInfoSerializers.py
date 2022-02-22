from rest_framework import serializers
from api.models import VehicleInfo

class VehicleInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleInfo
        fields = (
            'id', "year", "created_at", "updated_at"
        )
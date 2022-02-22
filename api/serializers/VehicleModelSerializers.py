from rest_framework import serializers
from api.serializers import VehicleCompanySerializer
from api.models import VehicleModel
class getVehicleModelSerializer(serializers.ModelSerializer):
    vehicle_company = VehicleCompanySerializer()
    class Meta:
        model = VehicleModel
        fields = (
           'id', 'vehicle_company', 'name',  "created_at", "updated_at"
        )

class VehicleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = (
           'id', 'vehicle_company', 'name',  "created_at", "updated_at"
        )
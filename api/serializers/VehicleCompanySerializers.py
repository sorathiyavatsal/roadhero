from rest_framework import serializers
from api.models import VehicleCompany
class VehicleCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleCompany
        fields = (
           'id', 'name', 'icon', "created_at", "updated_at"
        )
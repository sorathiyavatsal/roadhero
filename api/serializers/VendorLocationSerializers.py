from rest_framework import serializers
from api.serializers import getUserSerializer
from api.models import VenderLocation

class getVenderLocationSerializer(serializers.ModelSerializer):
    user = getUserSerializer()
    class Meta:
        model = VenderLocation
        fields = (
           'id', 'user', 'latitude', 'longitude', 'address', "created_at", "updated_at"
        )

class VenderLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenderLocation
        fields = (
            'id', 'user', 'latitude', 'longitude', 'address', "created_at", "updated_at"
        )
    def update(self, instance, validated_data):
        if 'latitude' in validated_data:
            instance.latitude = validated_data.get('latitude', instance.latitude)
        elif 'longitude' in validated_data:
            instance.longitude = validated_data.get('longitude', instance.longitude)
        elif 'address' in validated_data:
            instance.address = validated_data.get('address', instance.latitude)
        instance.save()
        return super(VenderLocationSerializer, self).update(instance, validated_data)
from rest_framework import serializers
from api.serializers import ServiceSerializer, getUserSerializer
from api.models import Trip
class getTripSerializer(serializers.ModelSerializer):
    user = getUserSerializer()
    vendor = getUserSerializer()
    service = ServiceSerializer()
    class Meta:
        model = Trip
        fields = (
           'id', 'user', 'vendor', 'service', 'source_lat_lng',
            'source_address', 'destination_lat_lng', 'destination_address',
            'start_time', 'end_time', 'trip_path', 'map_image', "created_at", "updated_at"
        )

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = (
           'id', 'user', 'vendor', 'service', 'source_lat_lng',
            'source_address', 'destination_lat_lng', 'destination_address',
            'start_time', 'end_time', 'trip_path', 'map_image', "created_at", "updated_at"
        )
    def update(self, instance, validated_data):
        if 'map_image' in validated_data:
            instance.map_image = validated_data.get('map_image', instance.map_image)
        elif 'end_time' in validated_data:
            instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.save()
        return super(TripSerializer, self).update(instance, validated_data)
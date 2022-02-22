from rest_framework import serializers
from api.models import BookingHistory, PackageDelivery
from api.serializers import ServiceSerializer, getVehicleModelSerializer, VehicleColorSerializer, VehicleInfoSerializer, getUserSerializer
from geopy.geocoders import GoogleV3
from decouple import config

class getBookingHistorySerializer(serializers.ModelSerializer):
    vehicle = getVehicleModelSerializer()
    vendor = getUserSerializer()
    vehicle_color = VehicleColorSerializer()
    vehicle_year = VehicleInfoSerializer()
    service = ServiceSerializer()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    address = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    class Meta:
        model = BookingHistory
        fields = (
           'id', 'vehicle', 'vehicle_color', 'vehicle_year', 'vendor', 'service', 'rating', 'name', 'mobile', 'email',
            'latitude', 'longitude', 'payment_status', 'price', 'promo_code', 'rating',
           'service_note', 'created_at', 'address'

        )

    def get_address(self, obj):
        geocoder = GoogleV3(api_key=config("MAP_KEY"))
        location_list = geocoder.reverse((obj.latitude, obj.longitude))
        address = str(location_list)
        return address

    def get_price(self, obj):
        total_price = obj.price
        return total_price


class BookingHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = BookingHistory
        fields = (
            'id', 'vehicle', 'vehicle_color', 'vehicle_year', 'vendor', 'service', 'rating', 'name', 'mobile', 'email',
            'latitude', 'longitude', 'payment_status', 'price', 'promo_code',
            'service_note'
        )

    def update(self, instance, validated_data):
        if 'rating' in validated_data:
            instance.rating = validated_data.get('rating', instance.rating)
        elif 'payment_status' in validated_data:
            instance.payment_status = validated_data.get('payment_status', instance.payment_status)
        elif 'price' in validated_data:
            instance.payment_status = validated_data.get('price', instance.payment_status)

        instance.save()
        return super(BookingHistorySerializer, self).update(instance, validated_data)

class PackageDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageDelivery
        fields = (
            'id', 'request_id', 'delivery_from', 'delivery_to', 'details'
        )
from rest_framework import serializers
from api.serializers import getUserSerializer
from api.serializers.bookingSerializers import getBookingHistorySerializer
from api.models import serviceRequest

class getServiceRequestSerializer(serializers.ModelSerializer):
    request_id = getBookingHistorySerializer()
    vendor_id = getUserSerializer()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    price = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    class Meta:
        model = serviceRequest
        fields = (
           'id', 'request_id',  "vendor_id", "request_status", "service_status",
           "price", "rating", "review", "created_at", "is_deleted", "image1", "step",
            "image2", "image3", "image4", "eta", "arrived", "completed", "images", "signature"
        )
    def get_price(self, obj):
        total_price = obj.request_id.service.price
        return total_price

    def get_images(self, obj):
        image_data = [obj.image1, obj.image2, obj.image3, obj.image4]
        images = [x for x in image_data if x]
        return images


class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = serviceRequest
        fields = (
            'id', 'request_id',  "vendor_id", "request_status", "service_status",
            "rating", "review", "created_at", "is_deleted", "image1",
            "image2", "image3", "image4", "signature", "terms", "eta",
            "arrived", "completed", "step"
        )
    def update(self, instance, validated_data):
        if 'rating' in validated_data:
            instance.rating = validated_data.get('rating', instance.rating)
        elif 'review' in validated_data:
            instance.review = validated_data.get('review', instance.review)
        elif 'request_status' in validated_data:
            instance.request_status = validated_data.get('request_status', instance.request_status)
        elif 'service_status' in validated_data:
            instance.service_status = validated_data.get('service_status', instance.service_status)
        elif 'image1' in validated_data:
            instance.image1 = validated_data.get('image1', instance.image1)
        elif 'image2' in validated_data:
            instance.image2 = validated_data.get('image2', instance.image2)
        elif 'image3' in validated_data:
            instance.image3 = validated_data.get('image3', instance.image3)
        elif 'image4' in validated_data:
            instance.image4 = validated_data.get('image4', instance.image4)
        elif 'signature' in validated_data:
            instance.signature = validated_data.get('signature', instance.signature)
        elif 'eta' in validated_data:
            instance.eta = validated_data.get('eta', instance.eta)
        elif 'arrived' in validated_data:
            instance.arrived = validated_data.get('arrived', instance.arrived)
        elif 'completed' in validated_data:
            instance.completed = validated_data.get('completed', instance.completed)
        elif 'step' in validated_data:
            instance.step = validated_data.get('step', instance.step)
        instance.save()
        return super(ServiceRequestSerializer, self).update(instance, validated_data)
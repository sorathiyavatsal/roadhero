from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()
from api.serializers import RoleSerializer
from api.models import VenderDetails
import base64
from api.utils import decode_base64
from django.core.files.base import ContentFile


class getUserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    class Meta:
        model = User
        fields = (
           "id", "first_name", "last_name", "email", "role",
            "phone", "profile_pic", "rating", "code", "status", "service_status",
            "card_token", "verified", "created_at", "updated_at", "device_token",
           'latitude', 'longitude'
        )

class crudUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id", "first_name", "last_name", "email", "role", 'password',
            "phone", "profile_pic", "rating", "code", "status", "service_status",
            "card_token", "verified", "created_at", "updated_at", "device_token",
            'latitude', 'longitude'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        elif 'first_name' in validated_data:
            instance.first_name = validated_data.get('first_name', instance.first_name)
        elif 'last_name' in validated_data:
            instance.last_name = validated_data.get('last_name', instance.last_name)
        elif 'email' in validated_data:
            instance.email = validated_data.get('email', instance.email)
        elif 'device_token' in validated_data:
            instance.device_token = validated_data.get('device_token', instance.device_token)
        elif 'role' in validated_data:
            instance.role = validated_data.get('role', instance.role)
        elif 'phone' in validated_data:
            instance.phone = validated_data.get('phone', instance.phone)
        elif 'verified' in validated_data:
            instance.verified = validated_data.get('verified', instance.verified)
        elif 'service_status' in validated_data:
            instance.service_status = validated_data.get('service_status', instance.service_status)
        elif 'status' in validated_data:
            instance.status = validated_data.get('status', instance.status)
        elif 'services_id' in validated_data:
            instance.services_id = validated_data.get('services_id', instance.services_id)
        elif 'profile_pic' in validated_data:
            instance.profile_pic = validated_data.get('profile_pic', instance.profile_pic)
        elif 'code' in validated_data:
            instance.code = validated_data.get('code', instance.code)
        elif 'latitude' in validated_data:
            instance.latitude = validated_data.get('latitude', instance.latitude)
        elif 'longitude' in validated_data:
            instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.save()
        return super(crudUserSerializer, self).update(instance, validated_data)

class VendorDetailSerializer(serializers.ModelSerializer):
    w9_form = serializers.FileField(required=False)
    driver_licence_front = serializers.FileField(required=False)
    ica_form = serializers.FileField(required=False)
    reg_insurence = serializers.FileField(required=False)
    background_check = serializers.FileField(required=False)
    authorization_form = serializers.FileField(required=False)
    class Meta:
        model = VenderDetails
        fields = (
            'id', 'user', 'w9_form',
            'driver_licence_front', 'ica_form', 'reg_insurence',
            'background_check', 'authorization_form'
        )
    # def update(self, instance, validated_data):
    #     if 'w9_form' in validated_data:
    #         instance.w9_form = validated_data.get('w9_form', instance.w9_form)
    #     elif 'driver_licence_front' in validated_data:
    #         instance.driver_licence_front = validated_data.get('driver_licence_front', instance.driver_licence_front)
    #     elif 'driver_licence_back' in validated_data:
    #         instance.driver_licence_back = validated_data.get('driver_licence_back', instance.driver_licence_back)
    #     elif 'reg_insurence' in validated_data:
    #         instance.reg_insurence = validated_data.get('reg_insurence', instance.reg_insurence)
    #     elif 'background_check' in validated_data:
    #         instance.background_check = validated_data.get('background_check', instance.background_check)
    #     elif 'authorization_form' in validated_data:
    #         instance.authorization_form = validated_data.get('authorization_form', instance.authorization_form)
    #     instance.save()
    #     return super(VendorDetailSerializer, self).update(instance, validated_data)

class getVendorDetailSerializer(serializers.ModelSerializer):
    user = getUserSerializer()
    class Meta:
        model = VenderDetails
        fields = (
            'id', 'user', 'w9_form',
            'driver_licence_front', 'ica_form', 'reg_insurence',
            'background_check', 'authorization_form'
        )
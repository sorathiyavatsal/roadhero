from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()
from api.models import chatModel
from api.serializers import getUserSerializer

class getChatSerializer(serializers.ModelSerializer):
    chat_to = getUserSerializer()
    chat_from = getUserSerializer()
    class Meta:
        model = chatModel
        fields = (
           'id', 'chat_to', 'chat_from', 'trip_id', 'message', 'chat_date'
        )

class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = chatModel
        fields = (
            'id', 'chat_to', 'chat_from', 'trip_id', 'message', 'chat_date'
        )

    def update(self, instance, validated_data):
        if 'message' in validated_data:
            instance.message = validated_data.get('message', instance.message)
        instance.save()
        return super(ChatSerializer, self).update(instance, validated_data)
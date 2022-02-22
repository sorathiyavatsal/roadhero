from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()
from api.models import PaymentAccount
from api.serializers import getUserSerializer


class PaymentAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentAccount
        fields = (
            'id', 'user', 'account_name', 'account_number', 'routing_number',
            'personal_id', 'address', 'zip_code', 'status'
        )
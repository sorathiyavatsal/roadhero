from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()
from api.models import Offer

class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields = (
           'id', 'name', 'promo_code', 'discount', 'detail'
        )
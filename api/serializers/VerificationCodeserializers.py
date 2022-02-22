from rest_framework import serializers
from api.models import VerificationCode
class VerificationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationCode
        fields = (
           'id', 'user', 'code', "created_at", "updated_at"
        )
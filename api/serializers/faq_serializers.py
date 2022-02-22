from rest_framework import serializers
from api.models import FAQ

class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQ
        fields = (
            'id', 'question', 'answer', "faq_type"
        )
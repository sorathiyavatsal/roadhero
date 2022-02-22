from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()
from api.models import Review
from api.serializers import getUserSerializer

class getReviewSerializer(serializers.ModelSerializer):
    review_by = getUserSerializer()
    review_for = getUserSerializer()
    class Meta:
        model = Review
        fields = (
           'id', 'review_by', 'review_for', 'review', 'rating'
        )

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = (
            'id', 'review_by', 'review_for', 'review', 'rating'
        )

    def update(self, instance, validated_data):
        if 'rating' in validated_data:
            instance.rating = validated_data.get('rating', instance.rating)
        elif 'review' in validated_data:
            instance.review = validated_data.get('review', instance.review)
        instance.save()
        return super(ReviewSerializer, self).update(instance, validated_data)
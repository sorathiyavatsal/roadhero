from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

class VenderLocation(models.Model):
    """
    This model is used to save application types.
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, related_name='users_id', on_delete=models.CASCADE,
        blank=True, null=True
    )
    latitude = models.CharField(max_length=254, blank=True, null=True)
    longitude = models.CharField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    class Meta:
        db_table = 'vender_location'
        indexes = [
            models.Index(fields=[
                'id', 'user', 'latitude',
                'longitude', 'address'
            ])
        ]
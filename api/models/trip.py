from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
from api.models import Service

class Trip(models.Model):
    """
    This model is used to save trips.
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
                    User, related_name='user_id',
                    on_delete=models.CASCADE,
                    blank=True,
                    null=True
                     )
    vendor = models.ForeignKey(
        User, related_name='vendor_id',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    service = models.ForeignKey(
        Service, related_name='service_id',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    source_lat_lng = models.CharField(max_length=254, blank=True, null=True)
    source_address = models.CharField(max_length=254, blank=True, null=True)
    destination_lat_lng = models.CharField(max_length=254, blank=True, null=True)
    destination_address = models.CharField(max_length=254, blank=True, null=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    trip_path = models.CharField(max_length=254, blank=True, null=True)
    map_image = models.CharField(max_length=254, blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'trip'
        indexes = [
            models.Index(fields=[
                'id', 'user', 'vendor', 'service', 'source_lat_lng',
                'source_address', 'destination_lat_lng', 'destination_address',
                'start_time', 'end_time', 'trip_path', 'map_image'
            ])
        ]
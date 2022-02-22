from django.db import models
from api.models import Service, User
from api.models.booking_history import BookingHistory
from django_base64field.fields import Base64Field
from api.utils import *
class serviceRequest(models.Model):
    """
    This model is used to save users role.
    """
    id = models.AutoField(primary_key=True)
    request_id = models.ForeignKey(
        BookingHistory, related_name='request_ids',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    vendor_id = models.ForeignKey(
        User, related_name='vendor_ids',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    review = models.CharField(max_length=250, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    request_status = models.BooleanField(default=False)
    service_status = models.BooleanField(default=False)
    image1 = models.TextField(max_length=900000, blank=True, null=True)
    image2 = models.TextField(max_length=900000, blank=True, null=True)
    image3 = models.TextField(max_length=900000, blank=True, null=True)
    image4 = models.TextField(max_length=900000, blank=True, null=True)
    signature = models.TextField(max_length=900000, blank=True, null=True)
    terms = models.BooleanField(default=True)
    step = models.IntegerField(default=1)
    eta = models.TimeField(blank=True, null=True)
    arrived = models.TimeField(blank=True, null=True)
    completed = models.TimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'service_request'
        indexes = [
            models.Index(fields=['id', 'request_id',  "vendor_id", "request_status", "service_status", "step"])
        ]

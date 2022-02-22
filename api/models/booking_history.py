from django.db import models
from api.models import VehicleInfo, User, Service, VehicleColor, VehicleModel
from api.models.offers import Offer
from django_base64field.fields import Base64Field

class BookingHistory(models.Model):
    """
    This model is used to save users role.
    """
    id = models.AutoField(primary_key=True)
    vehicle = models.ForeignKey(
        VehicleModel, related_name='vehicle',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    vehicle_color = models.ForeignKey(
        VehicleColor, related_name='car_color',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    vehicle_year = models.ForeignKey(
        VehicleInfo, related_name='car_year',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    vendor = models.ForeignKey(
        User, related_name='servicemen',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    service = models.ForeignKey(
        Service, related_name='serviceids',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    offer = models.ForeignKey(
        Offer, related_name='offers',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    name = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    promo_code = models.CharField(max_length=250, blank=True, null=True)
    discount = models.IntegerField(default=0)
    service_note = models.TextField(max_length=1000, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    latitude = models.CharField(max_length=250, blank=True, null=True)
    longitude = models.CharField(max_length=250, blank=True, null=True)
    payment_status = models.BooleanField(default=False)
    price = models.IntegerField(blank=True, null=True)
    tip = models.IntegerField(blank=True, null=True)
    card_token = models.CharField(max_length=250, blank=True, null=True)
    cancelled_by = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return f"{self.mobile}({self.id})"
    class Meta:
        db_table = 'booking_history'
        indexes = [
            models.Index(fields=[
                'id', 'vehicle', 'vendor', 'service', 'rating', 'mobile',
                'latitude', 'longitude', 'payment_status', 'price', 'name', 'tip'
            ])
        ]

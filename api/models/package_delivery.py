from django.db import models
from .booking_history import BookingHistory

class PackageDelivery(models.Model):
    id = models.AutoField(primary_key=True)
    request_id = models.ForeignKey(
        BookingHistory, related_name="booking_request_id",
        on_delete=models.CASCADE
    )
    delivery_from = models.CharField(max_length=250, blank=True, null=True)
    delivery_to = models.CharField(max_length=250, blank=True, null=True)
    details = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"{self.id}({self.request_id})"
    class Meta:
        db_table = 'package_delivery'
        indexes = [
            models.Index(fields=[
                'id', 'request_id', 'delivery_from', 'delivery_to', 'details'
            ])
        ]
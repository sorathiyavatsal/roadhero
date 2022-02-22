from django.db import models
from api.models import VehicleModel, User, VehicleColor, VehicleCompany
class VehicleInfo(models.Model):
    """
    This model is used to save users role.
    """
    id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=250, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return f"{self.year}({self.id})"
    class Meta:
        db_table = 'vehicle_info'
        indexes = [
            models.Index(fields=['id', "year"])
        ]

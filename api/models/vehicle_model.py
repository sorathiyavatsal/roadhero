from django.db import models
from api.models import VehicleCompany
class VehicleModel(models.Model):
    """
    This model is used to save users role.
    """
    id = models.AutoField(primary_key=True)
    vehicle_company = models.ForeignKey(
        VehicleCompany, related_name='vehicle_company_id',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    name = models.CharField(max_length=250, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return f'{self.name}({self.id})'

    class Meta:
        db_table = 'vehicle_model'
        indexes = [
            models.Index(fields=[
                'id', 'vehicle_company', 'name'
            ])
        ]

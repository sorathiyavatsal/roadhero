from django.db import models
from django.utils import timezone
from api.utils import *
from django.contrib.auth import get_user_model
User = get_user_model()

class VenderDetails(models.Model):
    """
    This model is used to save application types.
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, related_name='vendor_details', on_delete=models.CASCADE,
        blank=True, null=True
    )
    w9_form = models.FileField(upload_to=path_and_rename, blank=True, null=True)
    driver_licence_front = models.FileField(upload_to=path_and_rename, blank=True, null=True)
    ica_form = models.FileField(upload_to=path_and_rename, blank=True, null=True)
    reg_insurence = models.FileField(upload_to=path_and_rename, blank=True, null=True)
    background_check = models.FileField(upload_to=path_and_rename, blank=True, null=True)
    authorization_form = models.FileField(upload_to=path_and_rename, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.email}({self.id})"

    class Meta:
        db_table = 'user_details'
        indexes = [
            models.Index(fields=[
                'id', 'user', 'w9_form',
                'driver_licence_front', 'ica_form',  'reg_insurence',
                'background_check', 'authorization_form'
            ])
        ]
from django.db import models
from api.utils import path_and_rename

class Service(models.Model):
    """
    This model is used to save services.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    image = models.FileField(upload_to=path_and_rename, blank=True, null=True)
    detail = models.CharField(max_length=250, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    extra_price = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return f"{self.name}({self.id})"
    class Meta:
        db_table = 'service'
        indexes = [
            models.Index(fields=['id', 'name', 'image', 'detail', 'price'])
        ]

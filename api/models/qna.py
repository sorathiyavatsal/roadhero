from django.db import models
from api.models import Service
class QNaModel(models.Model):
    """
    This model is used to save users role.
    """
    id = models.AutoField(primary_key=True)
    service = models.ForeignKey(
        Service, related_name='qna_service',
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

    class Meta:
        db_table = 'qna'
        indexes = [
            models.Index(fields=[
                'id', 'service', 'name'
            ])
        ]

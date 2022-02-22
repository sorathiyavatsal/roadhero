from django.db import models
from api.models import QNaModel
class QnaOptionModel(models.Model):
    """
    This model is used to save users role.
    """
    id = models.AutoField(primary_key=True)
    qna = models.ForeignKey(
        QNaModel, related_name='qna_id',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    option = models.CharField(max_length=250, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'qna_option'
        indexes = [
            models.Index(fields=[
                'id', 'qna', 'option'
            ])
        ]

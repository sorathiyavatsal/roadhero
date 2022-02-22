from django.db import models
from api.models import User
class Review(models.Model):
    """
    This model is used to save users role.
    """
    id = models.AutoField(primary_key=True)
    review_by = models.ForeignKey(
        User, related_name='review_by',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    review_for = models.ForeignKey(
        User, related_name='review_for',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    review = models.TextField(max_length=1000, blank=True, null=True)
    rating = models.SmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'review'
        indexes = [
            models.Index(fields=[
                'id', 'review_by', 'review_for', 'review', 'rating'
            ])
        ]

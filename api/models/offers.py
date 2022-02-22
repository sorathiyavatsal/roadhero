from django.db import models

class Offer(models.Model):
    """
    This model is used to save users role.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    promo_code = models.CharField(max_length=250, blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True, default=0, help_text="discount in percentage")
    detail = models.CharField(max_length=250, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'offer'
        indexes = [
            models.Index(fields=['id', 'name', 'promo_code', 'discount', 'detail'])
        ]

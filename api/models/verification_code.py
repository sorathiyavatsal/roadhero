from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
class VerificationCode(models.Model):
    """
    This model is used to save users role.
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, related_name='user_code',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    mobile = models.CharField(max_length=50, blank=True, null=True, unique=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    first_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    device_token = models.CharField(max_length=250, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return f"{self.mobile}({self.id})"
    class Meta:
        db_table = 'verification_code'
        indexes = [
            models.Index(fields=['id', 'user', 'mobile', 'code', 'first_name', 'last_name', 'email'])
        ]

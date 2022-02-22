from django.db import models
from api.utils import path_and_rename
from django_base64field.fields import Base64Field
from django.contrib.auth import get_user_model
User = get_user_model()

class PaymentAccount(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, related_name='user_account', blank=True, null=True, on_delete=models.CASCADE
    )
    account_name = models.CharField(max_length=250, blank=True, null=True)
    account_number = models.CharField(max_length=250, blank=True, null=True)
    routing_number = models.CharField(max_length=250, blank=True, null=True)
    personal_id = models.CharField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    zip_code = models.CharField(max_length=250, blank=True, null=True)
    front_image = Base64Field(max_length=900000, blank=True, null=True)
    back_image = Base64Field(max_length=900000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.account_name}({self.account_number})"

    class Meta:
        db_table = 'payment_account'
        indexes = [
            models.Index(fields=[
                'id', 'user', 'account_name', 'account_number', 'routing_number', 'personal_id', 'address',
                'zip_code'
            ])
        ]
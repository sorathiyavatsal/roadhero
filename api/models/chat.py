from django.db import models
from api.models import User, Trip
class chatModel(models.Model):
    """
    This model is used to save users role.
    """
    id = models.AutoField(primary_key=True)
    chat_to = models.ForeignKey(
        User, related_name='chat_to_user',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    chat_from = models.ForeignKey(
        User, related_name='chat_from_user',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    trip_id = models.ForeignKey(
        Trip, related_name='chat_trip',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    message = models.TextField(max_length=1000, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    chat_date = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'chats'
        indexes = [
            models.Index(fields=[
                'id', 'chat_to', 'chat_from', 'trip_id', 'message', 'chat_date'
            ])
        ]

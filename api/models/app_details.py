from django.db import models

class AppDetail(models.Model):
    """
    This model is used to save users role.
    """
    id = models.AutoField(primary_key=True)
    about_us = models.TextField(max_length=1000, blank=True, null=True)
    office_number = models.CharField(max_length=50, blank=True, null=True)
    help_number = models.CharField(max_length=50, blank=True, null=True)
    about_email = models.CharField(max_length=50, blank=True, null=True)
    help_email = models.CharField(max_length=50, blank=True, null=True)
    help = models.TextField(max_length=1000, blank=True, null=True)
    booking_text = models.TextField(max_length=1000, blank=True, null=True)
    terms = models.TextField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'App detail'
        indexes = [
            models.Index(fields=['id', 'about_us', 'help'])
        ]

class FAQ(models.Model):
    """
    This model is used to save users role.
    """
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=50, blank=True, null=True)
    answer = models.TextField(max_length=1000, blank=True, null=True)
    faq_type = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'faq'
        indexes = [
            models.Index(fields=['id', 'question', 'answer', "faq_type"])
        ]
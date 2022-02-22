from __future__ import unicode_literals
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.db import models
from django.db import transaction

from api.models import Role
from api.utils import path_and_rename

class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email,and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model.
    """
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=True)

    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=254, blank=False)
    phone = models.CharField(max_length=17, blank=True, null=True, unique=True)
    profile_pic = models.FileField(blank=True, null=True, upload_to=path_and_rename)
    rating = models.IntegerField(default=0)
    code = models.IntegerField(blank=True, null=True)
    card_token = models.CharField(max_length=254, blank=True, null=True)
    customer_id = models.CharField(max_length=254, blank=True, null=True)
    device_token = models.CharField(max_length=254, blank=True, null=True)
    verified = models.BooleanField(default=False)
    role = models.ForeignKey(
        Role, related_name='role',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    services_id = models.CharField(max_length=254, blank=True, null=True)
    latitude = models.CharField(max_length=254, blank=True, null=True)
    longitude = models.CharField(max_length=254, blank=True, null=True)
    service_status = models.BooleanField(default=False)
    doc_verify = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

    class Meta:
        db_table = 'auth_user'
        indexes = [
            models.Index(fields=[
                'id', 'first_name', 'last_name', 'email', 'is_active',
                'latitude', 'longitude', 'services_id'
            ])
        ]
from django.db import models
from auths.managers import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    login_id = models.CharField(max_length=30, unique=True, null=False, blank=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'login_id'

    class Meta:
        db_table = 'user'
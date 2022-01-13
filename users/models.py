from django.db.models import EmailField, BooleanField, DateTimeField
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = EmailField(_("email address"), unique=True, db_index=True)
    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=True)
    time_create = DateTimeField(auto_now_add=True)
    time_update = DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"User {self.email}"

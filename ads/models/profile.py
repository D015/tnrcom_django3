from django.db.models import (
    Model,
    OneToOneField,
    PROTECT,
    CharField,
    DateField,
    ImageField,
)
from django.conf import settings

from users.models import CustomUser
from .base_mixin import BaseMixin


class Profile(BaseMixin, Model):
    user: CustomUser = OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=PROTECT
    )

    first_name = CharField(max_length=150, blank=True)
    last_name = CharField(max_length=150, blank=True)
    date_of_birth = DateField(blank=True, null=True)
    photo = ImageField(upload_to="photos/%Y/%m/%d", blank=True)

    def __str__(self):
        return f"Profile for user {self.user.email}"

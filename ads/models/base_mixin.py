from uuid import uuid4 as uuid_uuid4

from django.db.models import UUIDField, DateTimeField, BooleanField, Model


class BaseMixin(Model):

    uuid = UUIDField(
        db_index=True, default=uuid_uuid4, editable=False
    )

    time_create = DateTimeField(auto_now_add=True)
    time_update = DateTimeField(auto_now=True)
    active = BooleanField(default=True)
    archived = BooleanField(default=False)

    class Meta:
        abstract = True

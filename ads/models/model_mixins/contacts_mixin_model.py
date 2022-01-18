from django.db.models import Model, CharField


class ContactsMixinModel(Model):
    phone = CharField(max_length=50, blank=True)
    telegram = CharField(max_length=50, blank=True)
    address = CharField(max_length=250, blank=True)

    class Meta:
        abstract = True

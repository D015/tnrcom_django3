from django.db.models import Model, OneToOneField, PROTECT

from ads.models.profile_model import Profile


class RelationProfileMixinModel(Model):
    profile = OneToOneField(Profile, on_delete=PROTECT)

    class Meta:
        abstract = True

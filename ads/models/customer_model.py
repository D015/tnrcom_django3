from django.db.models import Model

from .model_mixins import BaseMixinModel
from .model_mixins import ContactsMixinModel
from .model_mixins import RelationProfileMixinModel


class Customer(
    BaseMixinModel, RelationProfileMixinModel, ContactsMixinModel, Model
):
    db_table = "customer"

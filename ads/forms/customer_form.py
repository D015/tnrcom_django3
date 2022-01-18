from django.forms import ModelForm

from .form_mixins import ContactsMixinForm
from ..models import Customer


class CustomerForm(ModelForm, ContactsMixinForm):
    class Meta:
        model = Customer
        fields = ["phone", "telegram", "address"]

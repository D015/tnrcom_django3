from django.forms import CharField, TextInput


class ContactsMixinForm:
    phone = CharField(widget=TextInput(attrs={"class": "form-input"}))
    telegram = CharField(widget=TextInput(attrs={"class": "form-input"}))
    address = CharField(widget=TextInput(attrs={"class": "form-input"}))

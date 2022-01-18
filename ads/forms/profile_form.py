from django.forms import CharField, ModelForm, TextInput, DateField, DateInput

from ..models import Profile


class ProfileForm(ModelForm):

    first_name = CharField(widget=TextInput(attrs={"class": "form-input"}))
    last_name = CharField(widget=TextInput(attrs={"class": "form-input"}))
    # TODO format="%Y-%m-%d" - this may not work on some local browser settings
    date_of_birth = DateField(
        widget=DateInput(
            attrs={"type": "date", "class": "form-input"}, format="%Y-%m-%d"
        )
    )

    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "date_of_birth"]

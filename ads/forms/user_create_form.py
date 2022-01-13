from django.forms import EmailField, EmailInput, CharField, PasswordInput
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):

    email = EmailField(
        label="Email", widget=EmailInput(attrs={"class": "form-input"})
    )

    password1 = CharField(
        label="Пароль",
        widget=PasswordInput(attrs={"class": "form-input"}),
    )

    password2 = CharField(
        label="Повтор пароля",
        widget=PasswordInput(attrs={"class": "form-input"}),
    )

    class Meta:
        model = get_user_model()
        fields = ("email", "password1", "password2")

        """Form stdout"""
        # widgets = {
        #     'email': forms.EmailInput(),
        #     'password1': forms.PasswordInput(),
        #     'password2': forms.PasswordInput(),
        # }

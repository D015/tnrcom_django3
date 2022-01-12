from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from ads.forms import RegisterUserForm
from ads.models import Profile


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'ads/user_create.html'

    def form_valid(self, form):
        # TODO try if db error while saving user
        user = form.save()
        try:
            Profile.objects.create(user=user)
        except ValueError:
            print("ValueError. When creating a profile, user - ValueError")
        else:
            login(self.request, user)
        return redirect('home')

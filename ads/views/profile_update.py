from django.urls import reverse_lazy
from django.views.generic import UpdateView

from ads.models import Profile
from ads.forms import ProfileForm


class ProfileUpdate(UpdateView):
    model = Profile
    form_class = ProfileForm
    # pk_url_kwarg = "pk"
    template_name = "ads/profile_update.html"
    # success_url = '/blog/manage_post_list'
    success_url = reverse_lazy("home")

    def get_object(self, queryset=None):
        return Profile.objects.get(uuid=self.kwargs.get("uuid"))


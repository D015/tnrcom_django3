from ads.models import Profile

from django.views.generic import DetailView


class ProfileDetail(DetailView):
    model = Profile
    template_name = "ads/profile_detail.html"
    context_object_name = "profile"

    def get_object(self, queryset=None):
        return Profile.objects.get(uuid=self.kwargs.get("uuid"))

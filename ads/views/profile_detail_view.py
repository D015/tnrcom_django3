from django.views.generic import DetailView

from ..models import Profile


class ProfileDetailView(DetailView):
    model = Profile
    template_name = "ads/profile_detail.html"
    context_object_name = "profile"

    def get_object(self, queryset=None):
        return Profile.objects.get(uuid=self.kwargs.get("uuid"))

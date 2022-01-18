from django.views.generic import CreateView

from ..models import Customer
from ..forms import CustomerForm


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "ads/profile_update.html"
    success_url = "/"
    raise_exception = True

    def form_valid(self, form):
        print()
        form.instance.profile = self.request.user.profile
        return super(CustomerCreateView, self).form_valid(form)

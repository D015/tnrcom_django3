# from typing import Union
#
# from django.views.generic import DetailView
# from django.views.generic.edit import CreateView, UpdateView
#
#
# class ObjectUUIDMixinView:
#     model = None
#
#     def get_object(
#             self: Union[CreateView, DetailView,
#                         UpdateView], queryset=None
#     ):
#         return self.model.objects.get(uuid=self.kwargs.get("uuid"))

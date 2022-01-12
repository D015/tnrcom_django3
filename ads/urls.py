from django.urls import path

from ads.views import index, RegisterUser, _ex

urlpatterns = [
    path('', index, name='home'),
    path('', _ex, name='_ex'),
    path('register/', RegisterUser.as_view(), name='register'),
]

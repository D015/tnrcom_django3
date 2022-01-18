from django.urls import path

from .views import (
    index,
    UserCreateView,
    _ex,
    ProfileDetailView,
    ProfileUpdateView,
    CustomerCreateView,
)

urlpatterns = [
    path("", index, name="home"),
    path("", _ex, name="_ex"),
    path("register/", UserCreateView.as_view(), name="register"),
    path(
        "profile/<uuid:uuid>/",
        ProfileDetailView.as_view(),
        name="profile_detail",
    ),
    path(
        "profile/update/<uuid:uuid>/",
        ProfileUpdateView.as_view(),
        name="profile_update",
    ),
    path(
        "customer-create/",
        CustomerCreateView.as_view(),
        name="customer_create",
    ),
]

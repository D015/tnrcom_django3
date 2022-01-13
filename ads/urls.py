from django.urls import path

from ads.views import index, UserCreate, _ex, ProfileDetail, ProfileUpdate

urlpatterns = [
    path("", index, name="home"),
    path("", _ex, name="_ex"),
    path("register/", UserCreate.as_view(), name="register"),

    path(
        "profile/<uuid:uuid>/",
        ProfileDetail.as_view(),
        name="profile_detail",
    ),

    path(
        "profile/update/<uuid:uuid>/",
        ProfileUpdate.as_view(),
        name="profile_update",
    ),
]

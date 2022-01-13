from django.shortcuts import render


def index(request):
    context = {
        "title": "Title сайт",
        "user_email": request.user.email,
        "user_profile_uuid": request.user.profile.uuid,
    }
    return render(request, "ads/index.html", context=context)

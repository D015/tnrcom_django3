from django.shortcuts import render


def index(request):
    data = {
        "title": "Title сайт",
        "user_email": request.user.email,
        "user_profile_uuid": request.user.profile.uuid,
        # "user_profile_customer": request.user.profile.customer,
        "user_profile_customer_address": request.user.profile.customer.address,
        "user_profile_customer_telegram": request.user.profile.customer.telegram,
        "user_profile_customer_phone": request.user.profile.customer.phone,
    }
    context = {"data": data}
    return render(request, "ads/index.html", context=context)

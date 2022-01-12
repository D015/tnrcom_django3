from django.http import HttpResponse


def _ex(request):
    request.readline()
    return HttpResponse(f"Страница приложения."
                        f" | {request.get_host()}"
                        f" | {request.get_port()}"
                        f" | {str(request.user)}"
                        f" | {request.user.email}"
                        f" | {request.user.password}"
                        f" | {request.user.profile}"
                        f" | {request.user.profile.uuid}"
                        f" | {type(request.user.profile.uuid)}"
                        f" | {request.method}")
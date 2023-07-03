from catalog.models import Logging

from django.urls import reverse


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        response = self.get_response(request)

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # if not request.path.startswith("/admin/"):
        if not request.path.startswith(reverse("admin:index")):
            Logging.objects.create(
                path=request.path,
                method=request.method,
                query_data=request.POST,
                body_data=request.POST,
                json_data=dict(request.POST),
            )
        else:
            pass

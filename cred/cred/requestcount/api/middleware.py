from requestcount.models import UserRequest
from django.db import IntegrityError, transaction

class RequestCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        with transaction.atomic():
            count=UserRequest.objects.get(pk=1)
            count.requests+=1
            count.save()
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response
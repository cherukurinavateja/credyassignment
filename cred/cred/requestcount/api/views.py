from rest_framework.decorators import api_view
from rest_framework.response import Response

from requestcount.models import UserRequest




@api_view(['GET', ])
def request_count_middleware(request):
    counter= UserRequest.objects.get(pk=1)
    req_counter=counter.requests
    response={"requests": str(req_counter)+" served by this server till now"}
    return Response(response)
    

@api_view(['GET', ])
def request_count_reset_middleware(request):
    counter= UserRequest.objects.get(pk=1)
    counter.requests= 0
    counter.save()
    response={"requests": "request count reset successful"}
    return Response(response)
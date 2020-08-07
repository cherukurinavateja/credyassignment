from django.urls import path
from requestcount.api.views import(
	request_count_middleware,
	request_count_reset_middleware,
)


app_name = 'requestcount'
# url for register counter/reset
urlpatterns = [
	path('request-count', request_count_middleware, name="request-count"),
	path('request-count/reset', request_count_reset_middleware, name="request-reset"),

]
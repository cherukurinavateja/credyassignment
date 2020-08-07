from django.urls import path
from moviecollection.api.views import(
	api_detail_collection_view,
	api_delete_collection_view,
	
)

app_name = 'moviecollection'

urlpatterns = [
	path('collection', api_detail_collection_view, name="detail"),
	path('collection/<collection_uuid>', api_delete_collection_view, name="delete"),
	
]
from django.urls import path

from movielist.api.views import(
	ApiMovieListView,
	api_movie_list,
)

app_name = 'movielist'

urlpatterns = [
	# path('movies', ApiMovieListView.as_view(), name="list"),
	path('movies/', api_movie_list, name="list"),
]
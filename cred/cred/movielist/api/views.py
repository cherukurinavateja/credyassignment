from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

from account.models import Account
from movielist.models import MovieLists
from movielist.api.serializers import MovieListSerializer
from movielist.api import utils


class ApiMovieListView(ListAPIView):
	queryset = MovieLists.objects.all()
	serializer_class = MovieListSerializer
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	pagination_class = PageNumberPagination

#Local url for movies hitting the original url 
@api_view(["GET",])
def api_movie_list(request):
	page_count= utils.movie_page_count()
	page_number = request.GET.get('page', None)
	def_url= 'https://demo.credy.in/api/v1/maya/movies/'
	def_url_pag= 'https://demo.credy.in/api/v1/maya/movies/?page=*'
	local_url= 'http://127.0.0.1:8000'
	local_url_pag= 'http://127.0.0.1:8000/movies/?page=*'
	
	if page_number is None:
		movie_list= utils.movieList(def_url)
		next_page= local_url_pag.replace('*',str(2))
		movie_list['next']= next_page
		movie_list['previous']= None
		page_count= movie_list['count']
		return Response(movie_list)

	elif (int(page_number) > 2) and (int(page_number) < page_count):

		url_to_sent= def_url_pag.replace('*',page_number)
		movie_list= utils.movieList(url_to_sent)
		next_page= local_url_pag.replace('*',str(int(page_number)+1))
		prev_page= local_url_pag.replace('*',str(page_number))
		movie_list['next']= next_page
		movie_list['previous']= prev_page
		return Response(movie_list)

	elif int(page_number)==2:
		url_to_sent= def_url_pag.replace('*',page_number)
		movie_list= utils.movieList(url_to_sent)
		next_page= local_url_pag.replace('*',str(int(page_number)+1))
		movie_list['next']= next_page
		movie_list['previous']= local_url
		return Response(movie_list)

	else:
		url_to_sent= def_url_pag.replace('*',page_number)
		movie_list= utils.movieList(url_to_sent)
		movie_list['next']= None
		movie_list['previous']= local_url_pag.replace('*',str(int(page_number)-1))
		return Response(movie_list)

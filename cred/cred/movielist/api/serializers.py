from rest_framework import serializers

from movielist.models import MovieLists


class MovieListSerializer(serializers.ModelSerializer):
	class Meta:
		model = MovieLists
		fields = ['title', 'description', 'genres','id']
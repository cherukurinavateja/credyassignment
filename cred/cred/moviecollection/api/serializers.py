from rest_framework import serializers

from moviecollection.models import Moviecollections


class MovieCollectionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Moviecollections
		fields = ['title', 'description', 'movies']
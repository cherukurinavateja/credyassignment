from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from collections import Counter

from account.models import Account
from movielist.models import MovieLists
from moviecollection.models import Moviecollections
from moviecollection.api.serializers import MovieCollectionSerializer
from django.core import serializers
import json

SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'successfully deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'

# Get top genres from User collection
def get_top_genres(movies):
    movies = list(set(movies))
    mv = MovieLists.objects.all()
    movie_json = json.loads(serializers.serialize("json", mv))
    genre_list = []
    for i in movie_json:
        if i["pk"] in movies:
            if 'fields' in i:
                if 'genres' in i['fields']:
                    genre_list.extend(i['fields']['genres'].split(","))
    genre_dct={}
    for i in genre_list:
        if i in genre_dct:
            genre_dct[i]+=1
        else:
            genre_dct[i]=1
    k = Counter(genre_dct)
    # Finding 3 highest values 
    top_three_genres = k.most_common(3)
    top_gen=[i[0] for i in top_three_genres]
    message= ','.join(top_gen)
    return message


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def api_detail_collection_view(request):

    if request.method == "GET":
        mv = Moviecollections.objects.all()
        collection_json = json.loads(serializers.serialize("json", mv))
        result = {
            'is_success': True,
            'data': {
                'collections': []
            }
        }
        collections = []
        movies = []
        for i in collection_json:
            if 'fields' in i:
                collections.append(i['fields'])
                if 'movies' in i['fields']:
                    for j in i['fields']['movies']:
                        movies.append(j)
        # Obtaining top genres
        top_genres = get_top_genres(movies)
        result['data']['collections'] = collections
        result['favourite_genres'] = top_genres
        return Response(result)

    if request.method == 'POST':
        req=request.data
        if len(req['movies']) != len(set(req['movies'])):
            return Response({"response": "duplicate movies entered"})
        collection_post = Moviecollections(author=request.user)
        serializer = MovieCollectionSerializer(
            collection_post, data=request.data)
        if serializer.is_valid():
            c_uid = serializer.save()
            data = {"response": "Success", "collection_uuid": c_uid.pk}
            return Response(data)
        return Response({"response": "Collection creation failed"})


@api_view(['PUT', 'DELETE', ])
@permission_classes((IsAuthenticated, ))
def api_delete_collection_view(request, collection_uuid):

    try:
        collection = Moviecollections.objects.filter(pk=collection_uuid)
    except collection.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = collection.delete()
        data = {}
        if operation:
            data['response'] = DELETE_SUCCESS
        return Response(data=data)

    if request.method == 'PUT':
        uid = Moviecollections.objects.get(pk=collection_uuid)
        collection_update = Moviecollections(author=request.user)
        serializer = MovieCollectionSerializer(uid, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {"response": "Collection successfully updated"}
            return Response(data)
        return Response({"response": "Collection update failed"})

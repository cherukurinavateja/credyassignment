from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from account.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token

# from account import middleware


@api_view(['POST', ])
def registration_view(request):

	if request.method == 'POST':
		serializer = RegistrationSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			account = serializer.save()
			data['response'] = 'successfully registered new user.'
			#getting the token for new user from db to display in response
			token = Token.objects.get(user=account).key
			data['access_token'] = token	
			# data['email'] = account.email
			# data['username'] = account.username
		else:
			data = serializer.errors
		return Response(data)



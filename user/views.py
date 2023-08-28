from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User 

from django.shortcuts import get_object_or_404




@api_view(['POST'])
def login(request):

    username = request.data['username']
    password = request.data['password']

    user = get_object_or_404(User, username=username)
    user = User.objects.get(username =username)

    if user.password == password:
        
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(instance=user)
        
        return Response({
            "token": token.key,
            "user": serializer.data,
        })
    
    return Response({
            "detail":"Not found."},
            status=status.HTTP_404_NOT_FOUND
        )




@api_view(['POST'])
def signup(request):
    
    serializer = UserSerializer(data=request.data)
    print(serializer)
    
    if serializer.is_valid():

        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])        
        token = Token.objects.create(user=user)

        return Response({
            "token" : token.key,
            "user" : serializer.data,
        })
    
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
    )

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    email = request.user.email
    print(email)
    return Response('Passed for {}'.format(email))

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

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
        },
        status=status.HTTP_200_OK)
    
    return Response({
            "detail":"Not found."},
            status=status.HTTP_404_NOT_FOUND
        )

"""Class using to login in this API."""
class LoginUserAPIView(APIView):



    """Receive a POST request, login the API and genereta token. """
    def post(self, request):

        username = request.data['username']
        password = request.data['password'] 

        try:
            user = User.objects.get(username=username)
            if user.password == password:
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserSerializer(instance=user)
                context = {
                    "token" : token.key,
                    "user" : user_serializer.data,
                }
                return Response(context, status=status.HTTP_200_OK)
            else:
                user = UserSerializer(data=request.data)                
                context = {
                    "ErrorLogin" : "Have any erro with login.",
                    "Data Login" : user.data,
                } 
                return Response(context,status=status.HTTP_404_NOT_FOUND)
        except:
            data = request.data
            user = UserSerializer(data=data)
            user.is_valid()
            context = {
                "ErrorLogin" : "Have any erro with login.",
                "Data Login" : user.data,
            } 
            return Response(context,status=status.HTTP_404_NOT_FOUND)




@api_view(['POST'])
def signup(request):
    
    serializer = UserSerializer(data=request.data)
    
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




class ListUsersAPIView(APIView):

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        data = users_serializer.data
        return Response(data, status=status.HTTP_200_OK)
    

class LogoutUserAPIView(APIView):
    """View to logout."""


    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def post(self, request, format=None):
        """
            Using the request.method to recovery what user request'it. 
            After that, destroy you token. If this view receive a request
            for anyone not login, return error.
        """

        user = request.user
        Token.objects.filter(user=user).delete()
        context = {
            "msg" : f"The user {user} has ben logut.",
        }
        return Response(context, status=status.HTTP_200_OK)

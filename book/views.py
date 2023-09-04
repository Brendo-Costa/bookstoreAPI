from rest_framework.response import Response
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (
    BaseAuthentication,
    SessionAuthentication,
    TokenAuthentication,
)
from rest_framework import status
from rest_framework.views import APIView


"""Using to response all books after request."""


""" class BookListAPIView(generics.ListAPIView):
    API View using to list books.

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #authentication_classes = (BaseAuthentication, )
    #permission_classes = (IsAuthenticated, ) """

#1 - Reescrevendo todas as views usandoa penas APIView

class BookListAPIView(APIView):
    """This class return all of books store in db."""
    

    def get(self, request, format=None):

        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)    
    
######################################################################
""" class BookCreateAPIView(generics.CreateAPIView):
    API View using to create a new book instance.

    queryset = Book.objects.all()
    serializer_class = BookSerializer
 """


class BookCreateAPIView(APIView):
    """Class receive one request to create one book in db."""

    def post(self, request, format=None):

        data = request.data
        serializer = BookSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
####################################################################################
""""
class BookUpdateAPIView(generics.UpdateAPIView):
    API View using to update a book instance.

    queryset = Book.objects.all()
    serializer_class = BookSerializer
"""

class BookUpdateAPIView(APIView):
    """Class using to update books on the system."""

    def put(self, request, pk, format=None):

        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

####################################################################
"""
class BookDeleteAPIView(generics.DestroyAPIView):
    API View usingo to delete a book instance.

    queryset = Book.objects.all()
    serializer_class = BookSerializer
"""

class BookDeleteAPIView(APIView):
    """Class create to delete books in the db."""

    
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, format=None):

        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response({"msg": "Deleted."},status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({"msg": "Have no book with this pk"},status=status.HTTP_204_NO_CONTENT)
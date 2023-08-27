from rest_framework.response import Response
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


"""Using to response all books after request."""


class BookListAPIView(generics.ListAPIView):
    """API View using to list books."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateAPIView(generics.CreateAPIView):
    """API View using to create a new book instance."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateAPIView(generics.UpdateAPIView):
    """API View using to update a book instance."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteAPIView(generics.DestroyAPIView):
    """API View usingo to delete a book instance."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    
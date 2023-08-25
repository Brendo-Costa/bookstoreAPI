from .models import Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    
    available = serializers.ReadOnlyField()
    store = serializers.ReadOnlyField()
    class Meta:
        model = Book
        exclude = ['in_store']
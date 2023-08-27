from .models import Book, Category
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


class CategorySerializer(serializers.ModelSerializer):
    """Using to serializer category models."""

    class Meta:
        model = Category
        exclude = []


class BookSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    """Using to serializer book models."""

    available = serializers.ReadOnlyField()
    store = serializers.ReadOnlyField()
     
    class Meta:
        model = Book
        exclude = ['in_store']    
        
    category = CategorySerializer()

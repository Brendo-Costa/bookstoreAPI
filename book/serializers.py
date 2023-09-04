"""This codes means the serializers presents in the app."""
from .models import Book, Category
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer




class CategorySerializer(serializers.ModelSerializer):
    """Using to serializer category models."""

    class Meta:
        model = Category
        exclude = []


#WritableNestedModelSerializer ( Caso não deseje sobrescrever methodo create, use essa função)
class BookSerializer(serializers.ModelSerializer):
    """Using to serializer book models."""


    available = serializers.ReadOnlyField()
    store = serializers.ReadOnlyField()
    category = CategorySerializer()
    
    class Meta:
        model = Book
        exclude = ['in_store']    
        
    
    def create(self, validated_data):
        """Overyde the create method to implement category."""


        category_data = validated_data.pop('category') # Extraindo o dado referente ao atributo "category" dos dados validados usando o metodo "validated_data"
        category, created = Category.objects.get_or_create(**category_data) # Checa se tem uma categoria criada, ou cria uma com base nos dados de categoria extraidos.
        book = Book.objects.create(category=category, **validated_data) # Cria o livro, adicionando o atributo "category" ao modelo.
        return book
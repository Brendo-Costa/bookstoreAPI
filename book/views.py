from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book
# Create your views here.


"""Using to response all books after request."""
@api_view(['GET', 'POST'])

def books(request): 
    
    if request.method == 'GET':

        books = Book.objects.all()

        output = [{
            'name': book.name,
            'category': book.category,
            'author': book.author,
        } for book in books]
    
    elif request.method == 'POST':
        
        name = request.data.get('name')
        category = request.data.get('category')
        author = request.data.get('author')

        book = Book.objects.create(
            name = name,
            category = category,
            author = author,
        )

        output = {
            'name': book.name,
            'category': book.category,
            'author': book.author,
        } 
        
    return Response(output)
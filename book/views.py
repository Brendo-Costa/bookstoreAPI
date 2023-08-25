from rest_framework.response import Response
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer

# Create your views here.


"""Using to response all books after request."""
#@api_view(['GET', 'POST'])

class BookAPIView(APIView): 
    

    """Get method using to return all of the books store in the db."""
    def get(self, request):
        
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    
    """Post method using to read one object in db."""
    def post(self, request):

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
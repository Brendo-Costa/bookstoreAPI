from django.urls import path
from .views import BookAPIView

appname = 'book'

urlpatterns = [
    path('books/', BookAPIView.as_view() , name='all'),
]

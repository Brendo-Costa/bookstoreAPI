from django.urls import path
from .views import (
    BookListAPIView, 
    BookCreateAPIView, 
    BookUpdateAPIView,
    BookDeleteAPIView
)

appname = 'book'

urlpatterns = [
    path('books/list', BookListAPIView.as_view() , name='list'),
    path('books/create', BookCreateAPIView.as_view(), name='create'),
    path('books/update/<int:pk>', BookUpdateAPIView.as_view(), name='update'),
    path('books/delete/<int:pk>', BookDeleteAPIView.as_view(), name='delete'),
]

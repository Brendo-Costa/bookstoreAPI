from django.urls import path
from .views import (
    BookListAPIView, 
    BookCreateAPIView, 
    BookUpdateAPIView,
    BookDeleteAPIView
)

appname = 'book'

urlpatterns = [
    path('list/', BookListAPIView.as_view() , name='list'),
    path('create/', BookCreateAPIView.as_view(), name='create'),
    path('update/<int:pk>', BookUpdateAPIView.as_view(), name='update'),
    path('delete/<int:pk>', BookDeleteAPIView.as_view(), name='delete'),
]

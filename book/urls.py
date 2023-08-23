from django.urls import path
from .views import books

appname = 'book'

urlpatterns = [
    path('books/', books , name='all'),
]

from django.contrib import admin

# Register your models here.
from .models import Book

"""Register book model in django admin."""
admin.site.register(Book)
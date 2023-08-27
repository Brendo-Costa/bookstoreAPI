from django.contrib import admin

# Register your models here.
from .models import Book, Category

"""Register book model in django admin."""
admin.site.register([Book, Category])
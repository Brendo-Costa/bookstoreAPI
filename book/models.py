from django.db import models

# Create your models here.
class Book(models.Model):
    """Using to abstract a book."""

    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    author = models.CharField(max_length=30)

    def __str__(self):
        return self.name
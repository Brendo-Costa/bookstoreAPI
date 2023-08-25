from django.db import models

# Create your models here.
class Book(models.Model):
    """Using to abstract a book."""

    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    in_store = models.PositiveBigIntegerField(default=1)

    def available(self):
        return bool(self.in_store)
    
    def store(self):
        all = Book.objects.all()
        all = len(all)
        return all

    def __str__(self):
        return self.name
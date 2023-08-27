from django.db import models

class Category(models.Model):
    """Usingo to abstract book category."""

    category = models.CharField(max_length=30)
   
    def __str__(self):
        return self.category
    

# Create your models here.
class Book(models.Model):
    """Using to abstract a book."""

    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
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
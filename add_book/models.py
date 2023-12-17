from django.db import models

class BookAdd(models.Model):
    bookName = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    publicationYear = models.CharField(max_length=8)
    volume = models.IntegerField()
    remarks = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.bookName
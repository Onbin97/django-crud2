from django.db import models

class Book(models.Model):
    title        = models.CharField(max_length=45)
    release_date = models.DateField()
    price        = models.IntegerField()
    to_author    = models.ManyToManyField("Author", through="Bookauthor", related_name="to_book")
#   authors = 
    class Meta:
        db_table = "books"

class Author(models.Model):
    name = models.CharField(max_length=45)
    age  = models.IntegerField()
    Univ = models.CharField(max_length=45)

    class Meta:
        db_table = "authors"

class Bookauthor(models.Model):
    book   = models.ForeignKey("Book", on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    class Meta: 
        db_table = "books_authors"



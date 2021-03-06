import uuid

from django.conf import settings
from django.db import models
from isbn_field import ISBNField


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    website = models.URLField()

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


COVER_TYPES_CHOICES = (('hardcover', 'Hardcover'), ('paperback', 'Paperback'),)
BOOK_LANGUAGE_CHOICES = (('PL', 'Polish'), ('EN', 'English'),)


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='catalogue number')
    title = models.CharField(db_index=True, max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    description = models.TextField()
    publication_date = models.DateField()
    image_url = models.URLField()
    cover = models.CharField(max_length=9, choices=COVER_TYPES_CHOICES, default='paperback')
    language = models.CharField(max_length=2, choices=BOOK_LANGUAGE_CHOICES, default='PL')
    isbn = ISBNField(db_index=True)

    def get_last_comments(self, qt=settings.BOOK_LAST_COMMENTS):
        return self.comments.filter(is_removed=False, is_public=True).order_by('-submit_date')[:qt]

    def __str__(self):
        return self.title

import json
from urllib.parse import urljoin

from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework.response import Response

from books.models import Publisher, Author, Book
from comments.models import Comment

User = get_user_model()


class BookBaseTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='johny_bravo')
        self.publisher = Publisher.objects.create(name='SuperPub', website='http://example.com')
        self.author = Author.objects.create(first_name='Freddy', last_name='Mercury')

        self.book = Book.objects.create(
            title='Nice Book',
            publisher=self.publisher,
            description='desc..',
            publication_date=timezone.now(),
            image_url='http://exammple.com',
            isbn='9788328336148'
        )
        self.book.authors.add(self.author)

        self.create_comments_for_book(self.book, 6)

    def _get_last_comments(self):
        return Comment.objects.filter(
            is_removed=False,
            is_public=True
        ).order_by('-submit_date')[:settings.BOOK_LAST_COMMENTS]

    def create_comments_for_book(self, book, qt=5):
        comments = []
        for i in range(qt):
            comments.append(Comment(book=book, author=self.user, text='a' * 2))
        Comment.objects.bulk_create(comments)

    def assert_paginated_response(self, response: Response, expected_results: [dict]):
        """
        Assertion function for paginated responses
        """
        self.assertEqual(
            json.loads(response.content),
            {
                'count': len(expected_results),
                'next': None,
                'previous': None,
                'results': expected_results
            }
        )

    def create_author_json_reposnse(self, author: Author):
        """
        Create json like response object
        """
        return {
            'id': author.id,
            'first_name': author.first_name,
            'last_name': author.last_name,
            'api_url': self.get_api_url(reverse('author-detail', kwargs={'pk': author.pk})),

        }

    def create_commment_json_response(self, books_id: str, comment: Comment):
        """
        Create json like response object
        """
        return {
            'author': f'{comment.author}',
            'text': comment.text,
            'submit_date': f'{comment.submit_date.date()}T{comment.submit_date.time()}Z',
            'api_url': self.get_api_url(reverse('book-comments-detail',
                                                kwargs={'books_pk': books_id,'pk': comment.pk})),
        }

    def create_book_json_response(self, book: Book, publisher: Publisher, authors: [dict]):
        """
        Create json like response object
        """
        return {
            'id': f'{book.id}',
            'title': book.title,
            'authors': authors,
            'publisher': {
                'name': publisher.name,
                'id': publisher.pk,
                'website': publisher.website,
                'api_url': self.get_api_url(reverse('publisher-detail', kwargs={'pk': publisher.pk})),
            },
            'publication_date': f'{book.publication_date.date()}',
            'image_url': book.image_url,
            'cover': book.cover,
            'language': book.language,
            'last_comments': [
                self.create_commment_json_response(str(book.id), comment) for comment in self._get_last_comments()
            ],
            'isbn': book.isbn,
            'api_url': self.get_api_url(reverse('book-detail', kwargs={'pk': f'{book.pk}'})),
        }


    def get_api_url(self, path):
        return urljoin('http://testserver', path)

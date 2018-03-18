import datetime
import json

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase

from books.models import Book, Author, Publisher

User = get_user_model()


class BookHubAPITestCase(APITestCase):

    def assert_paginated_response(self, response: Response, expected_results: [dict]):
        """
        Assertion function for paginated responses
        """
        self.assertEqual(
            json.loads(response.content.decode('utf8')),
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
            'last_name': author.last_name
        }

    def create_book_json_response(self, book: Book, publisher: Publisher, authors: [dict]):
        """
        Create json like response object
        """
        return {
            'title': book.title,
            'authors': authors,
            'publisher': {
                'name': publisher.name,
                'id': publisher.pk,
                'website': publisher.website
            },
            'publication_date': f'{book.publication_date.date()}',
            'image_url': book.image_url,
            'cover': book.cover,
            'language': book.language,
            'isbn': book.isbn,
        }


class AuthorAPIViewTests(BookHubAPITestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name='Name', last_name='Surname')

    def test_author_listing(self):
        """
        Ensure we can list authors.
        """
        response = self.client.get(reverse('author-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assert_paginated_response(
            response=response,
            expected_results=[
                {
                    'first_name': self.author.first_name,
                    'id': self.author.pk,
                    'last_name': self.author.last_name
                }
            ]
        )

    def test_show_author(self):
        """
        Ensure we can get author detail.
        """
        response = self.client.get(reverse('author-detail', kwargs={'pk': self.author.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            json.loads(response.content.decode('utf8')),
            {
                'first_name': self.author.first_name,
                'id': self.author.pk,
                'last_name': self.author.last_name
            }
        )


class AuthorAPIViewFilterTests(BookHubAPITestCase):

    def setUp(self):
        self.anabel = Author.objects.create(first_name='Anabel', last_name='Wol')
        self.casandra = Author.objects.create(first_name='Casandra', last_name='Strange')

    def test_author_filtered_by_first_name(self):
        """
        Ensure query param filtering by first name works
        """
        response = self.client.get(reverse('author-list'), {'first_name': 'Anabel'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assert_paginated_response(
            response=response,
            expected_results=[
                {
                    'first_name': self.anabel.first_name,
                    'id': self.anabel.pk,
                    'last_name': self.anabel.last_name
                }
            ]
        )

    def test_author_filtered_by_last_name(self):
        """
        Ensure query param filtering by last name works
        """
        response = self.client.get(reverse('author-list'), {'last_name': 'Strange'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assert_paginated_response(
            response=response,
            expected_results=[
                {
                    'first_name': self.casandra.first_name,
                    'id': self.casandra.pk,
                    'last_name': self.casandra.last_name
                }
            ]
        )

    def test_author_filtered_by_last_name_and_first_name(self):
        """
        Ensure query param filtering by last name and first name works
        """
        for query_filter, expected in [
            ({'first_name': 'Anabel', 'last_name': 'Strange'}, []),
            ({'first_name': 'Anabel', 'last_name': 'Wol'}, [{'first_name': self.anabel.first_name,
                                                             'id': self.anabel.pk,
                                                             'last_name': self.anabel.last_name}]),
        ]:
            with self.subTest(filter=query_filter, expected=expected):
                response = self.client.get(reverse('author-list'), query_filter)
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assert_paginated_response(
                    response=response,
                    expected_results=expected
                )


class PublisherAPIViewTests(BookHubAPITestCase):
    def setUp(self):
        self.publisher_record = Publisher.objects.create(name='Super Pub', website='https://example.com/')

    def test_publisher_listing(self):
        """
        Ensure we can list publishers.
        """
        response = self.client.get(reverse('publisher-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assert_paginated_response(
            response=response,
            expected_results=[
                {
                    'name': self.publisher_record.name,
                    'id': self.publisher_record.pk,
                    'website': self.publisher_record.website
                }
            ]
        )

    def test_show_publisher(self):
        """
        Ensure we can get publisher detail.
        """
        response = self.client.get(reverse('publisher-detail', kwargs={'pk': self.publisher_record.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            json.loads(response.content.decode('utf8')),
            {
                'name': self.publisher_record.name,
                'id': self.publisher_record.pk,
                'website': self.publisher_record.website
            }
        )


class PublisherAPIViewFilterTests(BookHubAPITestCase):

    def test_publishers_filtered_by_name(self):
        """
        Ensure query param filtering by name works
        """
        publisher = Publisher.objects.create(name='Super Pub', website='https://example.com/')
        publisher_2 = Publisher.objects.create(name='Super Old', website='https://example.com/')  # noqa

        response = self.client.get(reverse('publisher-list'), {'name': 'Super Pub'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assert_paginated_response(
            response=response,
            expected_results=[
                {
                    'name': publisher.name,
                    'id': publisher.pk,
                    'website': publisher.website
                }
            ]
        )


class BookAPIViewTests(BookHubAPITestCase):
    def setUp(self):
        self.author_record = Author.objects.create(first_name='Name', last_name='Surname')
        self.publisher_record = Publisher.objects.create(name='Super Pub', website='https://example.com/')
        self.book_record = Book.objects.create(
            title='Super Book',
            publisher=self.publisher_record,
            description='Desc...',
            publication_date=datetime.datetime.now(),
            image_url='https://example.com/',
            isbn='9781491989333'
        )
        self.book_record.authors.add(self.author_record)

    def test_books_listing(self):
        """
        Ensure we can list books.
        """
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assert_paginated_response(
            response=response,
            expected_results=[
                self.create_book_json_response(self.book_record, self.publisher_record,
                                               [self.create_author_json_reposnse(self.author_record)])]
        )

    def test_show_book(self):
        """
        Ensure we can get book detail.
        """
        response = self.client.get(reverse('book-detail', kwargs={'pk': self.book_record.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            json.loads(response.content.decode('utf8')),
            self.create_book_json_response(self.book_record, self.publisher_record,
                                           [self.create_author_json_reposnse(self.author_record)])
        )


class BookAPIViewFilterTests(BookHubAPITestCase):
    def setUp(self):
        self.publisher_record = Publisher.objects.create(name='Super Pub', website='https://example.com/')
        self.book_record_1 = Book.objects.create(
            title='Super Book',
            publisher=self.publisher_record,
            description='Desc...',
            publication_date=datetime.datetime.now(),
            image_url='https://example.com/',
            isbn='9781491989333'
        )
        self.author_anabel = Author.objects.create(first_name='Anabel', last_name='Wol')
        self.book_record_1.authors.add(self.author_anabel)

        self.book_record_2 = Book.objects.create(
            title='Some Book',
            publisher=self.publisher_record,
            description='Desc...',
            publication_date=datetime.datetime.now(),
            image_url='https://example.com/ee',
            isbn='9781491989323'
        )
        self.author_casandra = Author.objects.create(first_name='Casandra', last_name='Strange')
        self.book_record_2.authors.add(self.author_casandra)

    def test_books_filtered_by_authors_first_name(self):
        """
        Ensure query param filtering by author first name works
        """
        response = self.client.get(reverse('book-list'), {'author_first_name': 'Anabel'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assert_paginated_response(
            response=response,
            expected_results=[
                self.create_book_json_response(self.book_record_1, self.publisher_record,
                                               [self.create_author_json_reposnse(self.author_anabel)])]
        )

    def test_books_filtered_by_authors_last_name(self):
        """
        Ensure query param filtering by author last name works
        """
        response = self.client.get(reverse('book-list'), {'author_last_name': 'Strange'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assert_paginated_response(
            response=response,
            expected_results=[
                self.create_book_json_response(self.book_record_2, self.publisher_record,
                                               [self.create_author_json_reposnse(self.author_casandra)])]
        )

    def test_books_with_one_author_filtered_by_authors_first_name_and_author_last_name(self):
        """
        Ensure query param filtering by author first name and last name works in case single book author
        """
        for query_filter, expected in [
            ({'author_first_name': 'Anabel', 'author_last_name': 'Strange'}, []),
            ({'author_first_name': 'Anabel', 'author_last_name': 'Wol'},
             [self.create_book_json_response(self.book_record_1, self.publisher_record,
                                             [self.create_author_json_reposnse(self.author_anabel)])]),
        ]:
            with self.subTest(query_filter=query_filter, expected=expected):
                response = self.client.get(reverse('book-list'), query_filter)
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assert_paginated_response(
                    response=response,
                    expected_results=expected
                )

    def test_books_with_many_authors_filtered_by_authors_first_name_and_author_last_name(self):
        """
        Ensure query param filtering by author first name and last name works in case many book authors
        """
        self.maxDiff = None
        self.book_record_2.authors.add(self.author_anabel)
        for query_filter, expected in [
            ({'author_first_name': 'Anabel', 'author_last_name': 'Strange'},
             [self.create_book_json_response(self.book_record_2, self.publisher_record,
                                             [self.create_author_json_reposnse(self.author_anabel),
                                              self.create_author_json_reposnse(self.author_casandra)])]),
            ({'author_first_name': 'Anabel', 'author_last_name': 'Wol'},
             [self.create_book_json_response(self.book_record_1, self.publisher_record,
                                             [self.create_author_json_reposnse(self.author_anabel)]),
              self.create_book_json_response(self.book_record_2, self.publisher_record,
                                             [self.create_author_json_reposnse(self.author_anabel),
                                              self.create_author_json_reposnse(self.author_casandra)])
              ]),
        ]:
            with self.subTest(query_filter=query_filter, expected=expected):
                response = self.client.get(reverse('book-list'), query_filter)
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assert_paginated_response(
                    response=response,
                    expected_results=expected
                )

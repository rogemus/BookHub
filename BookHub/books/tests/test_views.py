import datetime
import json

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

from books.models import Book, Author, Publisher
from books.tests.book_test_helper import BookBaseTest

User = get_user_model()


class AuthorAPIViewTests(BookBaseTest):
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
            expected_results=[self.prepare_author_object(self.author)]
        )

    def test_show_author(self):
        """
        Ensure we can get author detail.
        """
        response = self.client.get(reverse('author-detail', kwargs={'pk': self.author.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            json.loads(response.content),
            self.prepare_author_object(self.author)
        )


class AuthorAPIViewFilterTests(BookBaseTest):

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
            expected_results=[self.prepare_author_object(self.anabel)]
        )

    def test_author_filtered_by_last_name(self):
        """
        Ensure query param filtering by last name works
        """
        response = self.client.get(reverse('author-list'), {'last_name': 'Strange'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assert_paginated_response(
            response=response,
            expected_results=[self.prepare_author_object(self.casandra)]
        )

    def test_author_filtered_by_last_name_and_first_name(self):
        """
        Ensure query param filtering by last name and first name works
        """
        for query_filter, expected in [
            ({'first_name': 'Anabel', 'last_name': 'Strange'}, []),
            ({'first_name': 'Anabel', 'last_name': 'Wol'}, [self.prepare_author_object(self.anabel)]),
        ]:
            with self.subTest(filter=query_filter, expected=expected):
                response = self.client.get(reverse('author-list'), query_filter)
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assert_paginated_response(
                    response=response,
                    expected_results=expected
                )


class PublisherAPIViewTests(BookBaseTest):
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
            expected_results=[self.prepare_publisher_object(self.publisher_record)]
        )

    def test_show_publisher(self):
        """
        Ensure we can get publisher detail.
        """
        response = self.client.get(reverse('publisher-detail', kwargs={'pk': self.publisher_record.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            json.loads(response.content),
            self.prepare_publisher_object(self.publisher_record)
        )


class PublisherAPIViewFilterTests(BookBaseTest):

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
            expected_results=[self.prepare_publisher_object(publisher)]
        )


class BookAPIViewTests(BookBaseTest):

    def test_books_listing(self):
        """
        Ensure we can list books.
        """
        self.maxDiff = None
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assert_paginated_response(
            response=response,
            expected_results=[
                self.create_book_json_response(self.book, self.publisher,
                                               [self.create_author_json_reposnse(self.author)])]
        )

    def test_show_book(self):
        """
        Ensure we can get book detail.
        """
        response = self.client.get(reverse('book-detail', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            json.loads(response.content),
            self.create_book_json_response(self.book, self.publisher,
                                           [self.create_author_json_reposnse(self.author)])
        )


class BookAPIViewFilterTests(BookBaseTest):
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
        self.maxDiff = None
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

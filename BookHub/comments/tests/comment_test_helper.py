import datetime

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase

from books.models import Author, Book, Publisher

User = get_user_model()


class CommentBaseTest(APITestCase):
    def setUp(self):
        self.email = 'cristy@example.com'
        self.username = 'cristy'
        self.password = 'password'
        self.user_cristy = User.objects.create_user(
            self.username,
            self.email,
            self.password,
        )

        self.author_record = Author.objects.create(first_name='Name', last_name='Surname')
        self.publisher_record = Publisher.objects.create(name='Super Pub', website='https://example.com/')
        self.book = Book.objects.create(
            title='Super Book',
            publisher=self.publisher_record,
            description='Desc...',
            publication_date=datetime.datetime.now(),
            image_url='https://example.com/',
            isbn='9781491989333',
        )
        self.book.authors.add(self.author_record)

        self.data = {
            'username': self.username,
            'password': self.password,
        }

    def get_token(self):
        response = self.client.post(reverse('login'), self.data, format='json')
        return response.data['token']

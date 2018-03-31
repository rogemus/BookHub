from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from django.utils import timezone

from books.models import Publisher, Author

User = get_user_model()


class AuthBaseTest(APITestCase):
    def setUp(self):
        self.joined = timezone.now()
        self.first_name = 'Cristy'
        self.last_name = 'Someone'
        self.email = 'cristy@example.com'
        self.username = 'cristy'
        self.password = 'password'
        self.user_cristy = User.objects.create_user(
            self.username,
            self.email,
            self.password,
            first_name=self.first_name,
            last_name=self.last_name,
            date_joined=self.joined,
            is_active=True,
        )

        self.data = {
            'username': self.username,
            'password': self.password,
        }

        self.publisher = Publisher.objects.create(name='SuperPub', website='http://example.com')
        self.author = Author.objects.create(first_name='Freddy', last_name='Mercury')

    def get_token(self):
        response = self.client.post(reverse('login'), self.data, format='json')
        return response.data['token']

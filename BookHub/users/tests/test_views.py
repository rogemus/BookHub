import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserViewSet(APITestCase):
    """
    Class with testes connected to user: creating, deleting, retrieving data
    """
    def setUp(self):
        """
        Create dummy user
        """
        self.user = User.objects.create(username='test_user', email='example@email.com', password='foobar')

    def test_users_listing_with_existing_user(self):
        """
        Test should check users listing with existing user
        """
        user = self.user
        response = self.client.get(reverse('user-list', kwargs={}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertTrue(len(data['results']) == 1)
        self.assertEqual(data['results'][0]['id'], user.id)

    def test_user_get_by_username(self):
        """
        Test should check getting user by username
        """
        response_get = self.client.get(reverse('user-detail', kwargs={'username': 'test_user'}))
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)

    def test_user_delete(self):
        """
        Test should check user deletion
        """
        response_delete = self.client.delete(reverse('user-detail', kwargs={'username': 'test_user'}))
        self.assertEqual(response_delete.status_code, status.HTTP_204_NO_CONTENT)
        response_get = self.client.get(reverse('user-detail', kwargs={'username': 'test_user'}))
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)

    def test_users_listing_without_existing_user(self):
        """
        Test should check users listing without existing user
        """
        User.delete(self.user)
        response = self.client.get(reverse('user-list', kwargs={}))
        data = json.loads(response.content)
        self.assertTrue(len(data['results']) == 0)

    def test_user_create(self):
        """
        Test should check creating user
        """
        response_create = self.client.post(
            reverse('user-list', kwargs={}),
            {
                'email': 'example@email.com',
                'username': 'created_user',
                'password': 'foobar'
            },
        )
        self.assertEqual(response_create.status_code, status.HTTP_201_CREATED)
        response_get = self.client.get(reverse('user-detail', kwargs={'username': 'created_user'}))
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)

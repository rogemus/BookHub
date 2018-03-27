from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class AuthBaseTest(APITestCase):
    def setUp(self):
        self.email = 'cristy@example.com'
        self.username = 'cristy'
        self.password = 'password'
        self.user_cristy = User.objects.create_user(
            self.username,
            self.email,
            self.password,
        )

        self.data = {
            'username': self.username,
            'password': self.password,
        }


class LoginViewTest(AuthBaseTest):
    def test_should_get_proper_user_info_and_token_after_logged_in(self):
        """
        Test should check if user info and token are returned
        """
        response = self.client.post(reverse('login'), self.data, format='json')
        self.assertEqual(response.data['username'], self.username)
        self.assertEqual(response.data['email'], self.email)
        self.assertTrue('token' in response.data)

    def test_should_fail_to_log_in(self):
        """
        Test should fail if we give bad credentials
        """
        self.data['password'] = 'some bad password'
        response = self.client.post(reverse('login'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['non_field_errors'][0], 'Unable to log in with provided credentials.')


class RegisterViewTest(AuthBaseTest):
    def setUp(self):
        self.username = 'new_user'
        self.email = 'email@example.com'
        self.new_user = {
            'username': self.username,
            'password': 'password',
            'email': self.email,
        }

    def test_should_register_user(self):
        """
        Test should register user in DB
        """
        response = self.client.post(reverse('register-list'), self.new_user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        uew_user = User.objects.first()
        self.assertEqual(uew_user.username, self.username)

    def test_should_get_user_info_and_token_after_successful_registration(self):
        """
        Test should check if user info and token are returned
        """
        response = self.client.post(reverse('register-list'), self.new_user, format='json')
        self.assertEqual(response.data['username'], self.username)
        self.assertEqual(response.data['email'], self.email)
        self.assertTrue('token' in response.data)

    def test_should_raise_username_already_taken_error(self):
        """
        Test should check if user with taken username can't register
        """
        response = self.client.post(reverse('register-list'), self.new_user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(reverse('register-list'), self.new_user, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['username'][0], 'This username is already taken.')

    def test_should_raise_username_not_valid(self):
        """
        Test should check if username is valid
        """
        self.new_user['username'] = 'b@d_username'
        response = self.client.post(reverse('register-list'), self.new_user, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['username'][0],
                         'Usernames can only use letters, numbers, underscores and periods.')

    def test_should_raise_email_already_taken_error(self):
        """
        Test should check if user with taken email can't register
        """
        response = self.client.post(reverse('register-list'), self.new_user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(reverse('register-list'), self.new_user, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email'][0], 'user with this email already exists.')

    def test_should_raise_password_validation_error(self):
        """
        Test should check if password validation is working
        """
        self.new_user['password'] = 'wrong'
        response = self.client.post(reverse('register-list'), self.new_user, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password'][0], 'Ensure this field has at least 8 characters.')

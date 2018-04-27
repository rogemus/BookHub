import json

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

from favourites.models import Favourite
from favourites.tests.favourites_test_helper import FavouriteBaseTest

User = get_user_model()


class FavouritesViewTest(FavouriteBaseTest):
    def test_favourites_listing_for_existing_user(self):
        """
        Test should check favorites books listing for user
        """
        Favourite.objects.create(book=self.book, user=self.user_cristy)

        response = self.client.get(reverse('user-favourites-list',
                                           kwargs={'users_username': self.user_cristy.username}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertTrue(len(data['results']) == 1)
        self.assertEqual(data['results'][0]['book']['id'], f'{self.book.id}')

    def test_if_authenticated_user_can_add_book_to_favourite(self):
        """
        Test should check if logged in users can add book to his favourites
        """
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.get_token())
        response = self.client.post(
            reverse('user-favourites-list', kwargs={'users_username': self.user_cristy.username}),
            {'book_id': self.book.id},
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = json.loads(response.content)
        self.assertEqual(data['book']['id'], f'{self.book.id}')

    def test_if_authenticated_user_can_delete_book_from_favourite(self):
        """
        Test should check if logged in users can delete book from his favourites
        """
        favourite = Favourite.objects.create(book=self.book, user=self.user_cristy)

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.get_token())
        response = self.client.delete(
            reverse('user-favourites-detail', kwargs={
                'users_username': self.user_cristy.username,
                'pk': favourite.pk
            }),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_if_unauthenticated_user_cant_add_book_to_favourite(self):
        """
        Test should check if only logged in users can add book as favourite
        """
        response = self.client.post(
            reverse('user-favourites-list', kwargs={'users_username': self.user_cristy.username}),
            {'book_id': self.book.id},
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_if_unauthenticated_user_cant_delete_book_to_favourite(self):
        """
        Test should check if only logged in users can delete book from his favourites
        """
        favourite = Favourite.objects.create(book=self.book, user=self.user_cristy)

        response = self.client.delete(
            reverse('user-favourites-detail', kwargs={
                'users_username': self.user_cristy.username,
                'pk': favourite.pk
            }),
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_should_not_be_able_to_add_book_other_user_to_favourite(self):
        """
        Test should check if user have edit access to only his own favourites
        """
        Favourite.objects.create(book=self.book, user=self.other_user)

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.get_token())
        response = self.client.post(
            reverse('user-favourites-list', kwargs={'users_username': self.other_user.username}),
            {'book_id': 'f2fed9bf-63b0-47a6-907f-087072b5bf1f'},
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_should_not_be_able_to_delete_book_other_user_from_favourite(self):
        """
        Test should check if user have edit access to only his own favourites
        """
        favourite = Favourite.objects.create(book=self.book, user=self.other_user)

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.get_token())
        response = self.client.delete(
            reverse('user-favourites-detail', kwargs={
                'users_username': self.other_user.username,
                'pk': favourite.pk
            }),
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class FavouritesValidatorsViewTest(FavouriteBaseTest):
    def test_if_error_raised_when_user_add_to_favourite_book_that_not_exist(self):
        """
        Test should check if only existing books can be added as favourite
        """
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.get_token())
        response = self.client.post(
            reverse('user-favourites-list', kwargs={'users_username': self.user_cristy.username}),
            {'book_id': 'f2fed9bf-63b0-47a6-907f-087072b5bf1f'},
        )
        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(data['book_id'][0], f'Book with id: f2fed9bf-63b0-47a6-907f-087072b5bf1f does not exist.')

    def test_if_error_raised_when_user_add_to_favourite_book_that_already_is_added(self):
        """
        Test should check if user can't add same book to favourite
        """
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.get_token())
        self.client.post(
            reverse('user-favourites-list', kwargs={'users_username': self.user_cristy.username}),
            {'book_id': self.book.id},
        )
        response = self.client.post(
            reverse('user-favourites-list', kwargs={'users_username': self.user_cristy.username}),
            {'book_id': self.book.id},
        )
        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(data['message'][0], 'You have already added this book to your favourites.')


class FavouritesStabilitiViewTest(FavouriteBaseTest):
    def test_should_check_if_404_when_ask_for_not_exist_username(self):
        response = self.client.get(reverse('user-favourites-list', kwargs={'users_username': 'not_exist_user'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

import datetime
import json
import uuid

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Author, Publisher, Book
from comments.models import Comment

User = get_user_model()


class CommentViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user', email='ecs@email.com')

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

    def test_comments_listing_for_existing_book(self):
        """
        Test should check comment listing_for_book
        """
        comment = Comment.objects.create(
            book=self.book,
            author=self.user,
            text='This is comment',
        )
        response = self.client.get(reverse('book-comments-list', kwargs={'books_pk': self.book.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertTrue(len(data['results']) == 1)
        self.assertEqual(data['results'][0]['id'], comment.id)

    def test_if_only_public_and_not_deleted_comments_are_exposed_in_listing(self):
        """
        Test should check if only public and marked as non deleted comments are presented
        """
        comment = Comment.objects.create(
            book=self.book,
            author=self.user,
            text='This is comment',
            is_removed=False,
            is_public=True,
        )
        Comment.objects.create(book=self.book, author=self.user, is_removed=True, is_public=True,
                               text='deleted_comment', )
        Comment.objects.create(book=self.book, author=self.user, is_removed=False, is_public=False,
                               text='non_public_comment', )
        Comment.objects.create(book=self.book, author=self.user, is_removed=True, is_public=False,
                               text='non_public_and_deleted_comment', )

        response = self.client.get(reverse('book-comments-list', kwargs={'books_pk': self.book.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertTrue(len(data['results']) == 1)
        self.assertEqual(data['results'][0]['id'], comment.id)

    def test_if_authenticated_user_can_add_comments_to_book(self):
        """
        Test should check if logged in users can add comments
        """
        self.client.force_authenticate(self.user)
        response = self.client.post(
            reverse('book-comments-list', kwargs={'books_pk': self.book.pk}),
            {'text': 'New comment'},
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = json.loads(response.content)
        self.assertEqual(data['text'], 'New comment')

    def test_if_author_of_added_comment_is_user_posting_comment(self):
        """
        Test should check if user creating comment is it owner
        """
        self.client.force_authenticate(self.user)
        response = self.client.post(
            reverse('book-comments-list', kwargs={'books_pk': self.book.pk}),
            {'text': 'New comment'},
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = json.loads(response.content)
        self.assertEqual(data['author'], self.user.username)

    def test_if_unauthenticated_user_cant_add_comments(self):
        """
        Test should check if only logged in users can add comments
        """
        response = self.client.post(
            reverse('book-comments-list', kwargs={'books_pk': self.book.pk}),
            {'text': 'New comment'},
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CommentViewStabilityTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='ecs@email.com')

    def test_comments_listing_for_non_existing_book(self):
        """
        Test should check if comments for non existing are handled properly
        """
        response = self.client.get(reverse('book-comments-list', kwargs={'books_pk': f'{uuid.uuid4()}'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertTrue(len(data['results']) == 0)

    def test_if_authenticated_user_cant_add_comments_to_non_existing_book(self):
        """
        Test should check if logged in user cant add comment for non existing book
        """
        self.client.force_authenticate(self.user)
        response = self.client.post(
            reverse('book-comments-list', kwargs={'books_pk': f'{uuid.uuid4()}'}),
            {'text': 'New comment'},
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

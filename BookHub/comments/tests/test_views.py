import json
import uuid

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from comments.models import Comment
from comments.tests.comment_test_helper import CommentBaseTest

User = get_user_model()


class CommentViewTest(CommentBaseTest):

    def test_comments_listing_for_existing_book(self):
        """
        Test should check comment listing_for_book
        """
        comment = Comment.objects.create(
            book=self.book,
            author=self.user_cristy,
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
            author=self.user_cristy,
            text='This is comment',
            is_removed=False,
            is_public=True,
        )
        Comment.objects.create(book=self.book, author=self.user_cristy, is_removed=True, is_public=True,
                               text='deleted_comment', )
        Comment.objects.create(book=self.book, author=self.user_cristy, is_removed=False, is_public=False,
                               text='non_public_comment', )
        Comment.objects.create(book=self.book, author=self.user_cristy, is_removed=True, is_public=False,
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
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.get_token())
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
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.get_token())
        response = self.client.post(
            reverse('book-comments-list', kwargs={'books_pk': self.book.pk}),
            {'text': 'New comment'},
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = json.loads(response.content)
        self.assertEqual(data['author'], self.user_cristy.username)

    def test_if_unauthenticated_user_cant_add_comments(self):
        """
        Test should check if only logged in users can add comments
        """
        response = self.client.post(
            reverse('book-comments-list', kwargs={'books_pk': self.book.pk}),
            {'text': 'New comment'},
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class CommentViewPermissionTest(CommentBaseTest):

    def setUp(self):
        super(CommentViewPermissionTest, self).setUp()
        self.cristy_comment = Comment.objects.create(
            book=self.book,
            author=self.user_cristy,
            text='This is Cristy comment',
        )
        self.user_jack = User.objects.create_user(
            'jack',
            'jack@email.com',
            'password',
        )
        self.jack_comment = Comment.objects.create(
            book=self.book,
            author=self.user_jack,
            text='This is Jack comment',
        )

    def test_authenticated_user_should_edit_his_comment_with_patch_method(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.get_token())
        response = self.client.patch(
            reverse('book-comments-detail', kwargs={'books_pk': self.book.pk, 'pk': self.cristy_comment.pk}),
            {'text': 'Comment edited'},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['text'], 'Comment edited')

    def test_authenticated_user_should_edit_his_comment_with_put_method(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.get_token())
        response = self.client.put(
            reverse('book-comments-detail', kwargs={'books_pk': self.book.pk, 'pk': self.cristy_comment.pk}),
            {'text': 'Comment edited'},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['text'], 'Comment edited')

    def test_authenticated_user_should_not_be_able_to_edit_not_owned_comment_with_patch_method(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.get_token())
        response = self.client.patch(
            reverse('book-comments-detail', kwargs={'books_pk': self.book.pk, 'pk': self.jack_comment.pk}),
            {'text': 'Comment edited'},
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_should_not_be_able_to_edit_not_owned_comment_with_put_method(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.get_token())
        response = self.client.put(
            reverse('book-comments-detail', kwargs={'books_pk': self.book.pk, 'pk': self.jack_comment.pk}),
            {'text': 'Comment edited'},
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_should_delete_his_comment(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.get_token())
        response = self.client.delete(
            reverse('book-comments-detail', kwargs={'books_pk': self.book.pk, 'pk': self.cristy_comment.pk}),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_authenticated_user_should_not_be_able_to_delete_not_owned_comment(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.get_token())
        response = self.client.delete(
            reverse('book-comments-detail', kwargs={'books_pk': self.book.pk, 'pk': self.jack_comment.pk}),
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CommentViewStabilityTest(CommentBaseTest):

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
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.get_token())
        response = self.client.post(
            reverse('book-comments-list', kwargs={'books_pk': f'{uuid.uuid4()}'}),
            {'text': 'New comment'},
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

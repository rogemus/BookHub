from django.contrib.auth import get_user_model

from comments.models import Comment
from comments.tests.comment_test_helper import CommentBaseTest

User = get_user_model()


class CommentModelTest(CommentBaseTest):
    def setUp(self):
        super(CommentModelTest, self).setUp()
        self.comment = Comment.objects.create(
            book=self.book,
            author=self.user_cristy,
            text='This is comment',
        )

    def test_should_mark_comment_as_removed_and_non_public(self):
        self.comment.mark_as_removed()
        removed_comment = Comment.objects.first()
        self.assertTrue(removed_comment.is_removed)
        self.assertFalse(removed_comment.is_public)

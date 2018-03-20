from django.contrib.auth import get_user_model
from books.tests.book_test_helper import BookBaseTest
from comments.models import Comment

User = get_user_model()


class BookModelTest(BookBaseTest):

    def setUp(self):
        super(BookModelTest, self).setUp()
        self.expected_qs = Comment.objects.filter(
            book=self.book.id,
            is_public=True,
            is_removed=False,
        ).order_by('-submit_date')[:2]

    def test_should_return_two_newest_comments_for_book(self):
        self.create_comments_for_book(self.book, 5)
        self.assertQuerysetEqual(self.book.get_last_comments(2), self.expected_qs, transform=lambda x: x)

    def test_should_return_two_newest_comment_which_are_not_removed_and_are_public(self):
        self.create_comments_for_book(self.book, 3)
        Comment.objects.create(book=self.book, author=self.user, text='comment', is_removed=True, is_public=True)
        Comment.objects.create(book=self.book, author=self.user, text='comment', is_removed=False, is_public=False)
        Comment.objects.create(book=self.book, author=self.user, text='comment', is_removed=False, is_public=True)
        self.assertQuerysetEqual(self.book.get_last_comments(2), self.expected_qs, transform=lambda x: x)

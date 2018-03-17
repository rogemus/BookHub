from django.contrib.auth import get_user_model
from django.test import TestCase

from books.models import Book, Author, Publisher
from comments.models import Comment

User = get_user_model()


class BookModelBaseTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='johny_bravo')
        self.publisher = Publisher.objects.create(name='SuperPub', website='http://example.com')
        self.author = Author.objects.create(first_name='Freddy', last_name='Mercury')

        self.book = Book.objects.create(
            title='Nice Book',
            publisher=self.publisher,
            description='desc..',
            publication_date='2018-03-16',
            image_url='http://exammple.com',
            isbn='9788328336148'
        )
        self.book.authors.add(self.author)

    def create_comments_for_book(self, book, qt=5):
        comments = []
        for i in range(qt):
            comments.append(Comment(book=book, author=self.user, text='a' * 2))
        Comment.objects.bulk_create(comments)


class BookModelTest(BookModelBaseTest):

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

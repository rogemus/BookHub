import random

from django.contrib.auth import get_user_model
from django.utils import timezone

from accounts.tests.test_views import AuthBaseTest
from books.models import Publisher, Author, Book
from favourites.models import Favourite

User = get_user_model()


class UserModelTest(AuthBaseTest):

    def setUp(self):
        super(UserModelTest, self).setUp()
        self.expected_qs = Favourite.objects.filter(
            user=self.user_cristy,
        ).order_by('-added_at')[:2]

    def create_favourite_books(self, n):
        publisher = Publisher.objects.create(name='SuperPub', website='http://example.com')
        author = Author.objects.create(first_name='Freddy', last_name='Mercury')
        isbn = 9788328336148
        for i in range(n):
            book = Book.objects.create(
                title='Nice Book',
                publisher=publisher,
                description='desc..',
                publication_date=timezone.now(),
                image_url='http://exammple.com',
                isbn=f'{random.randint(isbn, isbn + 100)}',
            )
            book.authors.add(author)
            Favourite.objects.create(book=book, user=self.user_cristy)

    def test_should_return_two_newest_favourite_for_user(self):
        self.create_favourite_books(10)
        self.assertQuerysetEqual(self.user_cristy.get_last_favourites(2), self.expected_qs, transform=lambda x: x)

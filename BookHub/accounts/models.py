import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.validators import username_validator
from books.models import Book


class BookHubUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, numbers, underscores and periods only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("This username is already taken."),
        },
    )
    email = models.EmailField(unique=True, blank=False)
    favourites = models.ManyToManyField(Book, through='favourites.Favourite')

    class Meta:
        db_table = 'book_hub_user'
        verbose_name = 'user'
        verbose_name_plural = "users"

    def get_last_favourites(self, qt=settings.USER_LAST_FAVOURITES):
        return self.favourite_set.all().order_by('-added_at')[:qt]

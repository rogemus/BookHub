from django.conf import settings
from django.db import models

from books.models import Book


class Favourite(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            ("book", "user"),
        )

    def __str__(self):
        return f'{self.user} ❤️ {self.book}'

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Comment(models.Model):
    book = models.ForeignKey('books.Book', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(null=False, blank=False, max_length=250)
    submit_date = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_public = models.BooleanField(default=True)
    is_removed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.text[:30]}{"..." if len(self.text) > 30 else ""}'

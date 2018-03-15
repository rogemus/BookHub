import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(null=False, blank=False, max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    visible = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.text[:30]}{'...' if len(self.text) > 30 else ''}"


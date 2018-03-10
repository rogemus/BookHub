import uuid

from django.db import models


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publishedDate = models.DateField()
    imageUrl = models.URLField()
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

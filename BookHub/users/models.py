from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class User(models.Model):
    username_validator = UnicodeUsernameValidator()
    email = models.EmailField(blank=False)

    username = models.CharField(max_length=30, unique=True, validators=[username_validator],)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.username

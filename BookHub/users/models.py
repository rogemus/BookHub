from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class User(models.Model):
    username_validator = UnicodeUsernameValidator()
    email = models.EmailField(blank=False)

    username = models.CharField(max_length=30, unique=True,
                                help_text='Required. 30 characters or fewer. Letters, digits and ''@/./+/-/_ only.',
                                validators=[username_validator],
                                error_messages={
                                    'unique': "A user with that username already exists.",
                                })

    password = models.CharField(max_length=64)

    def __str__(self):
        return self.username

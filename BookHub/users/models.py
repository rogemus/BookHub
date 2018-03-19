from django.db import models
from django.core import validators


class User(models.Model):
    email = models.EmailField(blank=False)

    username = models.CharField(max_length=30, unique=True,
                                help_text='Required. 30 characters or fewer. Letters, digits and ''@/./+/-/_ only.',
                                validators=[
                                    validators.RegexValidator(r'^[\w.@+-]+$',
                                                              'invalid', 'Enter a valid username. '
                                                                         'This value may contain only letters, numbers '
                                                                         'and @/./+/-/_ characters.'),
                                ],
                                error_messages={
                                    'unique': "A user with that username already exists.",
                                })

    password = models.CharField(max_length=64)

    def __str__(self):
        return self.username

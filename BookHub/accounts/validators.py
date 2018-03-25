from django.core import validators
from django.utils.translation import gettext_lazy as _


class UsernameValidator(validators.RegexValidator):
    regex = r'^[a-zA-Z0-9._]+$'
    message = _('Usernames can only use letters, numbers, underscores and periods.')

username_validator = UsernameValidator()

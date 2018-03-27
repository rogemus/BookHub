from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _


class UserCreationForm(BaseUserCreationForm):
    email = forms.EmailField(label=_("Email"), max_length=254)

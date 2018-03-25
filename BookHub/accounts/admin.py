from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import BookHubUser


class BookHubUserAdmin(admin.ModelAdmin):
    search_fields = ('email', 'username',)


admin.site.register(BookHubUser, UserAdmin)


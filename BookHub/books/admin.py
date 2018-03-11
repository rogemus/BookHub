from django.contrib import admin

from books.models import Book, Author, Publisher


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name',)


class PublisherAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'publisher',)
    readonly_fields = ('id',)
    search_fields = ('title', 'authors__first_name', 'authors__last_name', 'publisher__name', 'isbn',)
    autocomplete_fields = ('authors',)
    list_per_page = 25


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)

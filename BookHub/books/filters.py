import django_filters

from books.models import Author, Book


class BookFilter(django_filters.FilterSet):
    publisher_name = django_filters.CharFilter(name='publisher__name')
    author_first_name = django_filters.ModelMultipleChoiceFilter(
        name='authors__first_name',
        to_field_name='first_name',
        queryset=Author.objects.all()
    )
    author_last_name = django_filters.ModelMultipleChoiceFilter(
        name='authors__last_name',
        to_field_name='last_name',
        queryset=Author.objects.all()
    )

    class Meta:
        model = Book
        fields = (
            'title',
            'cover',
            'language',
            'isbn',
            'author_first_name',
            'author_last_name',
            'publisher_name',
            'authors',
        )

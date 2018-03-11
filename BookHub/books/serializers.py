from rest_framework import serializers

from books.models import Book, Author, Publisher


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'first_name',
            'last_name',
            'api_url'
        )


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = (
            'name',
            'website',
            'api_url'
        )


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    publisher = PublisherSerializer(read_only=True)

    class Meta:
        model = Book
        fields = (
            'title',
            'authors',
            'publisher',
            'publication_date',
            'image_url',
            'cover',
            'language',
            'isbn',
            'api_url'
        )

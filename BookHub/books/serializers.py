from rest_framework import serializers
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer

from books.models import Book, Author, Publisher
from comments.models import Comment


class CommentSerializer(NestedHyperlinkedModelSerializer):
    author = serializers.StringRelatedField()

    parent_lookup_kwargs = {
        'books_pk': 'book__pk',
    }

    class Meta:
        model = Comment
        fields = (
            'author',
            'text',
            'submit_date',
            'api_url',
        )
        extra_kwargs = {
            'api_url': {
                'view_name': 'book-comments-detail',
            },
        }


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id',
            'first_name',
            'last_name',
            'api_url',
        )


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = (
            'id',
            'name',
            'website',
            'api_url',
        )


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    publisher = PublisherSerializer(read_only=True)
    last_comments = CommentSerializer(
        source='get_last_comments',
        many=True,
        read_only=True,
    )

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'authors',
            'publisher',
            'publication_date',
            'image_url',
            'cover',
            'language',
            'isbn',
            'api_url',
            'last_comments',
        )

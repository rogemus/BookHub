from rest_framework import serializers

from books.models import Book, Author, Publisher
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = (
            'author',
            'text',
            'submit_date',
        )


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
    last_comments = serializers.SerializerMethodField(source='comments')

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
            'last_comments',
            'api_url'
        )

    def get_last_comments(self, book):
        serializer = CommentSerializer(book.get_last_comments(3), many=True)
        return serializer.data

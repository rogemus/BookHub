from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer

from books.models import Book
from books.serializers import AuthorSerializer, PublisherSerializer
from favourites.models import Favourite


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    publisher = PublisherSerializer(read_only=True)

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'image_url',
            'api_url',
            'authors',
            'publisher',
        )
        read_only = (
            'image_url',
            'title',
        )


class FavouriteSerializer(NestedHyperlinkedModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    book = BookSerializer(read_only=True)
    book_id = serializers.UUIDField(write_only=True)

    parent_lookup_kwargs = {
        'users_username': 'user__username',
    }

    class Meta:
        model = Favourite
        fields = (
            'added_at',
            'api_url',
            'book',
            'user',
            'book_id',
        )

        validators = [
            UniqueTogetherValidator(
                queryset=Favourite.objects.all(),
                fields=('book_id', 'user'),
                message='You have already added this book to your favourites.'
            )
        ]

        extra_kwargs = {
            'api_url': {
                'view_name': 'user-favourites-detail',
            },

        }

    def validate_book_id(self, value):
        """
        Check if book exist in DB, if so,
         save the book instance into serializer property to cache object for create method
        """
        try:
            self.book_instance = Book.objects.get(pk=value)
        except Book.DoesNotExist:
            raise serializers.ValidationError(detail=f'Book with id: {value} does not exist.')
        return value

    def create(self, validated_data):
        return Favourite.objects.create(book=self.book_instance, user=self.context['request'].user)

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer

from favourites.models import Favourite

User = get_user_model()


class FavouriteSerializer(NestedHyperlinkedModelSerializer):
    book = serializers.StringRelatedField(read_only=True)

    parent_lookup_kwargs = {
        'users_username': 'user__username',
    }

    class Meta:
        model = Favourite
        fields = (
            'book',
            'added_at',
            'api_url',
        )

        extra_kwargs = {
            'api_url': {
                'view_name': 'user-favourites-detail',
            },

        }


class UserSerializer(serializers.ModelSerializer):
    last_favourites = FavouriteSerializer(
        source='get_last_favourites',
        many=True,
        read_only=True,
    )

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'last_favourites',
        )

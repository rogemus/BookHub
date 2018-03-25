from rest_framework import serializers

from accounts.models import BookHubUser


class BookHubUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookHubUser
        fields = (
            'username',
            'password',
        )

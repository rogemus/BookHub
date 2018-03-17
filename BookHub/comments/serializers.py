from rest_framework import serializers
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = (
            'id',
            'author',
            'text',
            'submit_date',
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'author': {'read_only': True}
        }

import logging

from rest_framework import serializers
from comments.models import Comment

logger = logging.getLogger(__name__)


class CommentSerializer(serializers.ModelSerializer):
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

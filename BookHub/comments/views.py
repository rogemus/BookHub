from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from books.models import Book
from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentResultsSetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 30


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or edited.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = CommentSerializer
    pagination_class = CommentResultsSetPagination

    def get_queryset(self):
        return Comment.objects.filter(book=self.kwargs['books_pk']).order_by('-submit_date')

    def perform_create(self, serializer):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, pk=self.kwargs['books_pk'])
        serializer.save(
            author=self.request.user,
            book=book
        )

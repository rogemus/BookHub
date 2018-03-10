from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from books.models import Book
from books.serializers import BookSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all().order_by('-created_at')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = BookSerializer

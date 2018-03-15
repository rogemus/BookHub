from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, routers

from books.filters import BookFilter
from books.models import Book, Author, Publisher
from books.permissions import ReadOnlyPermission
from books.serializers import BookSerializer, AuthorSerializer, PublisherSerializer


class BookHubApi(routers.APIRootView):
    """
    Welcome in interactive BookHub Api
    """
    pass


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all().order_by('-publication_date')
    permission_classes = (ReadOnlyPermission,)
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = BookFilter


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows authors to be viewed or edited.
    """
    queryset = Author.objects.all()
    permission_classes = (ReadOnlyPermission,)
    serializer_class = AuthorSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('first_name', 'last_name',)


class PublisherViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows publishers to be viewed or edited.
    """
    queryset = Publisher.objects.all()
    permission_classes = (ReadOnlyPermission,)
    serializer_class = PublisherSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',)

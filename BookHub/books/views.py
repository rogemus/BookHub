from rest_framework import viewsets, routers
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from books.models import Book, Author, Publisher
from books.serializers import BookSerializer, AuthorSerializer, PublisherSerializer


class BookHubApi(routers.APIRootView):
    """
    Welcome in interactive BookHub Api
    """
    pass


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all().order_by('-publication_date')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be viewed or edited.
    """
    queryset = Author.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = AuthorSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows publishers to be viewed or edited.
    """
    queryset = Publisher.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PublisherSerializer

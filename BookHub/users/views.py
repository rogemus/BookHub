from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, routers

from users.models import User
from books.permissions import ReadOnlyPermission
from users.serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-username')
    permission_classes = (ReadOnlyPermission,)
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('email', 'username',)

from django.contrib.auth import get_user_model
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from favourites.models import Favourite
from favourites.permission import IsFavouriteOwnerOrReadOnly, ListAndRetriveAndCreateAndDeleteViewSet
from favourites.serializers import FavouriteSerializer

User = get_user_model()


class FavouriteResultsSetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 30


class FavouriteViewSet(ListAndRetriveAndCreateAndDeleteViewSet):
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = FavouriteSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsFavouriteOwnerOrReadOnly)
    pagination_class = FavouriteResultsSetPagination

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['users_username'])
        return Favourite.objects.filter(user=user).order_by('-added_at')

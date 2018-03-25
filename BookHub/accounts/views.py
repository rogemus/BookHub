from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.views import ObtainJSONWebToken

from accounts.models import BookHubUser
from accounts.serializers import BookHubUserSerializer



class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.DestroyModelMixin,
                                viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, `create`, `delete` and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """
    pass


class LoginView(ObtainJSONWebToken):
    """
    API View that receives a POST with a user's username and password.

    Returns a JSON Web Token that can be used for authenticated requests.
    """
    serializer_class = JSONWebTokenSerializer


class RegisterView(CreateListRetrieveViewSet):
    """
    API endpoint that allows to register user, get individual user and get list of all users
    """
    queryset = BookHubUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = BookHubUserSerializer
    lookup_field = 'username'


login_view = LoginView.as_view()

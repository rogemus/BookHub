from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.views import ObtainJSONWebToken
from accounts.serializers import UserCreateSerializer

User = get_user_model()


class CreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    A viewset that provides only `create` action.

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


class RegisterView(CreateViewSet):
    """
    API endpoint that allows to register user

    Returns a JSON Web Token that can be used for authenticated requests.
    """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserCreateSerializer

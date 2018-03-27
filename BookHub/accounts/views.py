from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.views import ObtainJSONWebToken

from accounts.permissions import ReadOnlyPermission
from accounts.serializers import UserCreateSerializer, AboutUserSerializer

User = get_user_model()


class LoginView(ObtainJSONWebToken):
    """
    API View that receives a POST with a user's username and password.

    Returns a JSON Web Token that can be used for authenticated requests.
    """
    serializer_class = JSONWebTokenSerializer


class Register(APIView):
    """
    API endpoint that allows to register user

    Returns a JSON Web Token that can be used for authenticated requests.
    """
    permission_classes = (AllowAny,)
    serializer_class = UserCreateSerializer

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class AboutUserView(APIView):
    """
    API endpoint that show detailed user info

    Based on user token
    """
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, ReadOnlyPermission)
    serializer_class = AboutUserSerializer

    def get(self, request):
        serializer = AboutUserSerializer(request.user)
        return Response(serializer.data)

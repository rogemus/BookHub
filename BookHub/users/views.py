from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-username')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = UserSerializer
    filter_fields = ('email', 'username',)


# @api_view(['GET', 'POST'])
# def register(request):
#     """
#     Register a new user
#     """
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'GET':
#         return Response(status=status.HTTP_403_FORBIDDEN)

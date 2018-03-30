from rest_framework import permissions, mixins, viewsets


class IsFavouriteOwnerOrReadOnly(permissions.BasePermission):
    """
    Global permission check for if path username is same as user session
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return view.kwargs['users_username'] == request.user.username


class ListAndRetriveAndCreateAndDeleteViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin,
                                              mixins.RetrieveModelMixin, mixins.ListModelMixin,
                                              viewsets.GenericViewSet):
    """
    A viewset that provides only `create` and 'delete', 'get', 'list' action.
    """
    pass

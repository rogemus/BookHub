from rest_framework import mixins, viewsets, permissions


class CreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    A viewset that provides only `create` action.
    """
    pass


class ReadOnlyPermission(permissions.BasePermission):
    """
    Global read only permission.
    """

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

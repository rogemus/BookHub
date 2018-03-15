from rest_framework import permissions


class ReadOnlyPermission(permissions.BasePermission):
    """
    Global read only permission.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False

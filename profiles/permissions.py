from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrAdminOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Return True, if request method is GET, HEAD, or OPTIONS,
        or, if current user is staff or object owner.
        """
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user or request.user.is_staff

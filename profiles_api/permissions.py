from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit its own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit its own profile"""
        if request.method in permissions.SAFE_METHODS:
            # Always allow GET, HEAD or OPTIONS requests.
            return True

        # Check if the user profile object which the current user is trying to access are the same
        return obj.id == request.user.id

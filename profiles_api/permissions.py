from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit its own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit its own profile"""
        if request.method in permissions.SAFE_METHODS:
            # Always allow GET, HEAD or OPTIONS requests.
            return True

        # Check if the user profile object which the current user (logged in) is trying to access are the same
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow user to update its own status"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to update its own status"""
        if request.method in permissions.SAFE_METHODS:
            # Always allow GET, HEAD or OPTIONS requests.
            return True

        # Check if the feed item object is related to the logged in user
        return obj.user_profile.id == request.user.id

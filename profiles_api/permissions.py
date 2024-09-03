from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allows user to edit only their profiles"""

    def has_object_permission(self, request, view, obj):
        """Checks if user trying to edit own profile"""
        if request.method in permissions.SAFE_METHODS: 
            return True 
        return obj.id == request.user.id
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def object_have_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user

        #snippet/views.
        

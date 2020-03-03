from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    message = 'You must be the owner of the object'
    safe_methods = ['GET', 'PUT']

    def has_permission(self, request, view):
        if request.method in self.safe_methods:
            return True

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

from rest_framework.permissions import SAFE_METHODS, BasePermission


class SafeMethodsOnly(BasePermission):

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj=None):
        return request.method in SAFE_METHODS

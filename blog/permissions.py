from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminUserOrReadOnly(BasePermission):
    message = 'you are not admin and can not add anything!'
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or
                    request.user and request.user.is_staff)
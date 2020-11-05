from rest_framework.permissions import BasePermission


class HasObjectPer(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

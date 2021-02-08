from rest_framework import permissions

# class BasePermission(object):
#     def has_permission(self, request, view):
#         """
#         return True if permission is granted
#         """
#         return True

#     def has_object_permission(self, request, view, obj):
#         """
#         return True if permission is granted
#         """
#         return True


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        #Write permissions are only allowed to the author of a post
        return obj.author == request.user

        

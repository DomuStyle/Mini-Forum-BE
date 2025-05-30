from rest_framework.permissions import BasePermission, SAFE_METHODS
        
class IsOwnerOrReadOnly(BasePermission):
    # defines a custom permission class, inheriting from BasePermission.

    def has_object_permission(self, request, view, obj):
        # method that checks whether the user has permission to perform an action on a specific object.
        
        if request.method in SAFE_METHODS:
            # if the HTTP request method is a safe method (like GET, HEAD, or OPTIONS),
            # allow read-only access by returning True.
            return True
        
        elif request.method == "DELETE":
            # if the request is a DELETE operation, check if the user is a superuser or the object's author.
            # the `bool()` ensures the return value is a boolean.
            return bool(request.user and (request.user.is_superuser or request.user == obj.author))
        
        else:
            # for all other request methods (like POST, PUT, PATCH), only allow access if the user is the author.
            return bool(request.user and request.user == obj.author)
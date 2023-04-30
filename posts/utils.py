import json
from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the object
        return obj.user == request.user

class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {
                'id': obj.id,
                'username': obj.username,
                'email': obj.email,
            }
        return super().default(obj)

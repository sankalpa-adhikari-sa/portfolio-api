from drf_spectacular.utils import extend_schema
from django.shortcuts import render
from rest_framework import generics,authentication,permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
    )

@extend_schema(tags=["users"])
class CreateUserView(generics.CreateAPIView):
    """create a new user in system."""
    serializer_class= UserSerializer
@extend_schema(tags=["users"])
class CreateTokenView(ObtainAuthToken):
    """create a new auth token for user"""
    serializer_class= AuthTokenSerializer
    renderer_classes= api_settings.DEFAULT_RENDERER_CLASSES
@extend_schema(tags=["users"])
class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes= [authentication.TokenAuthentication]
    permission_classes= [permissions.IsAuthenticated]


    def get_object(self):
        """retrive and return authenticated user"""
        return self.request.user

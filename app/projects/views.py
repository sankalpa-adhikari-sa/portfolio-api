"""views for Projects APIs"""

from drf_spectacular.utils import extend_schema
from django.shortcuts import render
from rest_framework import viewsets,mixins,status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from core.models import Projects,Tag
from projects import serializers

@extend_schema(tags=["projects"])
class ProjectsViewSet(viewsets.ModelViewSet):
    """View for manging projects APIs."""
    serializer_class= serializers.ProjectsDetailSerializer
    queryset= Projects.objects.all()
    authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticatedOrReadOnly]


    def get_queryset(self):
        return self.queryset.order_by('-id')

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ProjectsSerializer
        elif self.action == 'upload_image':
            return serializers.ProjectImageSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """create a new project."""
        serializer.save(user=self.request.user)

    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        """Upload image to project"""
        project= self.get_object()
        serializer= self.get_serializer(project, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@extend_schema(tags=["projects"])
class TagsViewSet(mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """Manage Tags in database"""
    serializer_class= serializers.TagSerializer
    queryset= Tag.objects.all()
    authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.order_by('-name')


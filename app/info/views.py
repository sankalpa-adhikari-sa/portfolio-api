"""views for Infos APIs"""

from drf_spectacular.utils import extend_schema
from django.shortcuts import render
from rest_framework import viewsets,mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from core.models import Education,Experience,Certificate,Message,Skill,SocialLink
from info import serializers

@extend_schema(tags=["Education"])
class EducationViewSet(mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    """Manage Education in database"""
    serializer_class= serializers.EducationSerializer
    queryset= Education.objects.all()
    authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.order_by('-created')

@extend_schema(tags=["Experience"])
class ExperienceViewSet(mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    """Manage Experience in database"""
    serializer_class= serializers.ExperienceSerializer
    queryset= Experience.objects.all()
    authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.order_by('-created')

@extend_schema(tags=["Skill"])
class SkillViewSet(mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    """Manage Skill in database"""
    serializer_class= serializers.SkillSerializer
    queryset= Skill.objects.all()
    authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.order_by('-created')

@extend_schema(tags=["Certificates"])
class CertificateViewSet(mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    """Manage Certificate in database"""
    serializer_class= serializers.CertificateSerializer
    queryset= Certificate.objects.all()
    authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.order_by('-created')

@extend_schema(tags=["SocialLinks"])
class SocialLinkViewSet(mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    """Manage Social links in database"""
    serializer_class= serializers.SocialLinkSerializer
    queryset= SocialLink.objects.all()
    authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.order_by('-created')

@extend_schema(tags=["Message"])
class MessageViewSet(mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    """Manage Message in database."""
    serializer_class= serializers.MessageSerializer
    queryset= Message.objects.all()
    authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.order_by('-created')




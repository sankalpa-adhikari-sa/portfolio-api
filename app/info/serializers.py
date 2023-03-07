"""serializers for info APIs"""
from rest_framework import serializers
from core.models import Education,Experience,Certificate,Message,Skill,SocialLink

class EducationSerializer(serializers.ModelSerializer):
    """Serializer for education"""
    class Meta:
        model = Education
        fields= ['id','title','period','college','id','created']
        read_only_fields= ['id','created']

class ExperienceSerializer(serializers.ModelSerializer):
    """Serializer for Experience"""
    class Meta:
        model = Experience
        fields= ['id','title','period','company','id','created']
        read_only_fields= ['id','created']


class SkillSerializer(serializers.ModelSerializer):
    """Serializer for Skill"""
    class Meta:
        model = Skill
        fields= ['id','skillname','body','type','id','created']
        read_only_fields= ['id','created']
class CertificateSerializer(serializers.ModelSerializer):
    """Serializer for Certificate"""
    class Meta:
        model = Certificate
        fields= ['id','title','period','platform','link','id','created']
        read_only_fields= ['id','created']

class SocialLinkSerializer(serializers.ModelSerializer):
    """Serializer for social link """
    class Meta:
        model = SocialLink
        fields= ['id','linkedin','github','kaggle','facebook','instagram','created']
        read_only_fields= ['id','created']

class MessageSerializer(serializers.ModelSerializer):
    """Serializer for Message. """
    class Meta:
        model = Message
        fields= ['id','firstname','lastname','email','Message','phone','interests','is_read','created']
        read_only_fields= ['id','created']
"""Serializers for Project APIs"""

from rest_framework import serializers
from core.models import Projects,Tag

class TagSerializer(serializers.ModelSerializer):
    """Serializer for tags"""
    class Meta:
        model = Tag
        fields= ['id','name']
        read_only_fields= ['id']

class ProjectsSerializer(serializers.ModelSerializer):
    """serializer for Projects"""
    tags= TagSerializer(many=True, required=False)
    class Meta:
        model = Projects
        fields= ['id','title','caption','type','status','created','tags','demo_link','github_link','kaggle_link','other_source_link','thumbnail']
        read_only_fields= ['id']

    def _get_or_create_tags(self,tags, project):
        """Handling getting or creating tags as needed"""
        auth_user = self.context['request'].user
        for tag in tags:
            tag_obj,created = Tag.objects.get_or_create(
                user= auth_user,
                **tag,
            )
            project.tags.add(tag_obj)

    def create(self, validated_data):
        """create a project"""
        tags= validated_data.pop('tags',[])
        project= Projects.objects.create(**validated_data)
        self._get_or_create_tags(tags, project)

        return project
    def update(self, instance, validated_data):
        """update project"""
        tags= validated_data.pop('tags',None)
        if tags is not None:
            instance.tags.clear()
            self._get_or_create_tags(tags, instance)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class ProjectsDetailSerializer(ProjectsSerializer):
    """serializer for projects detail view"""
    class Meta(ProjectsSerializer.Meta):
        fields = ProjectsSerializer.Meta.fields + ['description']

class ProjectImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to Projects"""
    class Meta:
        model=Projects
        fields= ['id','thumbnail']
        read_only_fields= ['id']
        # extra_kwargs = {'thumbnail':{'required':'True'}}

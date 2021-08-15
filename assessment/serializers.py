from rest_framework import serializers

from .models import Assessment, Tags


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['name']


class AssessmentSerializer(serializers.ModelSerializer):

    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Assessment
        exclude = ['id']

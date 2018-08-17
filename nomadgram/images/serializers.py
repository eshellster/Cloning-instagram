from rest_framework import serializers
from . import models


class ImagesSerializer(serializers.Serializer):
    class Meta:
        model = models.Images
        fields = '__all__'


class CommentSerializer(serializers.Serializer):
    class Meta:
        model = models.Comment
        fields = '__all__'


class LikeSerializer(serializers.Serializer):
    class Meta:
        model = models.Like
        fields = '__all__'

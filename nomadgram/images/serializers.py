# -*- encoding: utf-8 -*-
from rest_framework import serializers
from . import models


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Like
        fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True)
    likes = LikeSerializer(many=True)

    class Meta:
        model = models.Image
        fields = (
            "id",
            "created_at",
            "updated_at",
            "file",
            "location",
            "caption",
            "creator",
            "comments",
            "likes"
        )

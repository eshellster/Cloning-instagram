# -*- encoding: utf-8 -*-
from rest_framework import serializers
from . import models
from nomadgram.images import serializers as image_serizlizers


class UserProfileSerializer(serializers.ModelSerializer):

    images = image_serizlizers.CountImageSerializer(many=True)

    class Meta:
        model = models.User
        fields = (
            'username',
            'name',
            'bio',
            'website',
            'post_count',
            'followers_count',
            'following_count',
            'images',
        )


class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'id',
            'profile_image',
            'username',
            'name',
        )

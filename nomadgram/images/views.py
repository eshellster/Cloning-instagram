from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
# Create your views here.


class Feed(APIView):

    def get(self, request, format=None):

        user = request.user

        following_users = user.following.all()

        image_list = []

        for following_user in following_users:

            user_images = following_user.image_set.all()[:2]

            for image in user_images:

                image_list.append(image)

        sort_list = sorted(image_list, key=lambda image: image.created_at, reverse=True)

        serializer = serializers.ImagesSerializer(sort_list, many=True)

        return Response(serializer.data)

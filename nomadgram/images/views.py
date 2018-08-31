from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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


class LikeImage(APIView):

    def get(self, request, image_id, format=None):

        user = request.user

        try:
            found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            preExisiting_like = models.Like.objects.get(
                creator=user,
                image=found_image
            )
            preExisiting_like.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except models.Like.DoesNotExist:

            new_like = models.Like.objects.create(
                creator=user,
                image=found_image
            )

            new_like.save()

            return Response(status=status.HTTP_201_CREATED)

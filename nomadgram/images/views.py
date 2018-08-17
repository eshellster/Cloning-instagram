from rest_framework import APIView
from rest_framework.response import Response
from . import models, serializers
# Create your views here.


class ListAllImaages(APIView):

    def get(self, request, format=None):

        all_images = models.Image.objects.all()

        serializers = serializers.ImagesSerializer(all_images, many=True)

        return Response(data=serializers.data)

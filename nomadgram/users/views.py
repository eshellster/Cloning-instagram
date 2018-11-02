from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers


class ExploreUsers(APIView):

    def get(self, request, format=None):

        last_five = models.User.objects.all().order_by('-date_joined')[:5]

        serializer = serializers.ListUserSerializer(last_five, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


explore_users = ExploreUsers.as_view()


class FollowUser(APIView):

    def post(self, request, user_id, format=None):

        user = request.user

        try:
            user_to_follow = models.User.objects.get(id=user_id)
        except model.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user.following.add(user_to_follow)

        return Response(status=status.HTTP_200_OK)


follow_user = FollowUser.as_view()


class UnFollowUser(APIView):

    def post(self, request, user_id, format=None):

        user = request.user

        try:
            user_to_follow = models.User.objects.get(id=user_id)
        except model.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user.following.remove(user_to_follow)

        return Response(status=status.HTTP_200_OK)


un_follow_user = UnFollowUser.as_view()


class UserProfile(APIView):

    def get(self, request, username, format=None):

        try:
            found_user = models.User.objects.get(username=username)
        except models.User.DoseNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.UserProfileSerializer(found_user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


user_profile = UserProfile.as_view()


class UserFollowers(APIView):

    def get(self, request, username, format=None):

        try:
            found_user = models.User.objects.get(username=username)
        except models.User.DoseNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user_followers = found_user.followers.all()

        serializer = serializers.ListUserSerializer(user_followers, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


user_followers = UserFollowers.as_view()


class UserFollowing(APIView):

    def get(self, request, username, format=None):

        try:
            found_user = models.User.objects.get(username=username)
        except models.User.DoseNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user_following = found_user.following.all()

        serializer = serializers.ListUserSerializer(user_following, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


user_following = UserFollowing.as_view()


class FollowView(APIView):

    # follow 하기
    def post(self, request, user_id, format=None):

        user = request.user
        # follow할 유저 찾기
        try:
            user_to_follow = models.User.objects.get(id=user_id)
        except models.User.DoesNotExist:
            # follow할 유저를 못찾았을때
            return Response(status=status.HTTP_404_NOT_FOUND)

        # following에 추가해주기.
        user.following.add(user_to_follow)
        user.save()
        # 그리고 user가 다른 user를 following 하면 following 당하는 user의
        # follower에 following을 요청한 user 가 들어가야함.
        user_to_follow.followers.add(user)
        user.save()
        # 알림생성해주기.
        #create_notifications(creator, to, notification_type, image = None)
        notifications_views.create_notifications(user, user_to_follow, 'follow')

        return Response(status=status.HTTP_200_OK)


follow_view = FollowView.as_view()

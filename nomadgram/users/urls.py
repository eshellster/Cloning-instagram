from django.urls import path

from nomadgram.users.views import (
    explore_users,
    follow_user,
    un_follow_user,
    user_profile,
    user_followers,
    user_following,
    follow_view,
)

app_name = "users"
urlpatterns = [
    path("explore/", view=explore_users, name="explore_users"),
    path("<int:user_id>/follow", view=follow_user, name="follow_user"),
    path("<int:user_id>/unfollow", view=un_follow_user, name="un_follow_user"),
    path("<str:username>/", view=user_profile, name="user_profile"),
    path("<str:username>/followers", view=user_followers, name="user_followers"),
    path("<str:username>/following", view=user_following, name="user_following"),
    path("<int:user_id>/following", view=follow_user, name="follow_view"),
]

from django.urls import path

from nomadgram.users.views import (
    explore_users,
    follow_user,
    un_follow_user,
    user_profile,
    follow_view,
)

app_name = "users"
urlpatterns = [
    path("explore/", view=explore_users, name="explore_users"),
    path("<int:user_id>/follow", view=follow_user, name="follow_user"),
    path("<int:user_id>/unfollow", view=un_follow_user, name="un_follow_user"),
    path("<str:username>/", view=user_profile, name="user_profile"),
    path("<int:user_id>/following", view=follow_user, name="follow_view"),
]

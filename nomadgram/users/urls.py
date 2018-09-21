from django.urls import path

from nomadgram.users.views import (
    explore_users
)

app_name = "users"
urlpatterns = [
    path("explore/", view=explore_users, name="explore"),
]

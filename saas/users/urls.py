from django.urls import path
from .views import (
    create_user,
    user_login,
)

urlpatterns = [
    path("create-users", create_user, name="create-users-path"),
    path("login-users", user_login, name="login-users-path"),
]

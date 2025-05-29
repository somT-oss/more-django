from django.urls import path
from .views import (
    create_user,
    user_login,
    forgot_password,
    password_token_check,
    reset_password
)

urlpatterns = [
    path("create-users", create_user, name="create_users_path"),
    path("login-users", user_login, name="login_users_path"),
    path('forgot-password', forgot_password, name='forgot_password_path'),
    path('password-reset/<id_base64>/<token>', password_token_check, name='password_token_check_path'),
    path('reset-password', reset_password, name='reset_password_path'),
]

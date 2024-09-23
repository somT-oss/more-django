from django.urls import path
from .views import (
    UserAPIView
)

urlpatterns = [
    path("home", UserAPIView.as_view(), name="users:view-home-url")
]

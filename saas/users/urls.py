from django.urls import path
from .views import (
    UserAPIView
)

urlpatterns = [
    path("handler/", UserAPIView.as_view(), name="view-home-url")
]

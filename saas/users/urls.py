from django.urls import path
from .views import (
    view_home
)

urlpatterns = [
    path("home", view_home, name="users:view-home-url")
]

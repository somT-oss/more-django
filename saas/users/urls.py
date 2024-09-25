from django.urls import path
from .views import (
    create_buyers
)

urlpatterns = [
    path("create-buyers/", create_buyers, name="create-buyers-path")
]

from django.urls import path
from .views import (
    create_product
)

urlpatterns = [
    path('create-product', create_product, name='create-product-path')
]

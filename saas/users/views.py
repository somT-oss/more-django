from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializer import CreateCustomUserserializers, CustomUsersLoginSerializer
from products.models import Products
from products.serializer import CreateProductSeriallizers


@api_view(['POST'])
def create_user(request: Request) -> Response:
    """
    Post Endpoint for creating users'
    """
    serializer_class = CreateCustomUserserializers(data=request.data)
    if not serializer_class.is_valid():
        return Response(serializer_class.errorss, status.HTTP_400_BAD_REQUEST)

    first_name = serializer_class.validated_data.get("first_name")
    last_name = serializer_class.validated_data.get("last_name")
    serializer_class.save()

    message = {
        "message": f"Account successfully created for {first_name} {last_name}"
    }
    return Response(message, status.HTTP_201_CREATED)


@api_view(['POST'])
def user_login(request: Request) -> Response:
    """
    Post Endpoint for users' login
    """
    pass
    serializer_class = CustomUsersLoginSerializer(data=request.data)
    if not serializer_class.is_valid():
        return Response(serializer_class.errors, status.HTTP_400_BAD_REQUEST)

    try:
        email = serializer_class.validated_data.get('email')
        password = serializer_class.validated_data.get('password')

        user = authenticate(email=email, password=password)
        print(user)
        if user is None:
            return Response({
                "errors": "Invalid user details"
            }, status.HTTP_400_BAD_REQUEST)
        user_auth_token = RefreshToken.for_user(user)
        message = {
            "access": str(user_auth_token.access_token),
            "refresh": str(user_auth_token)
        }
        return Response(message, status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "errors": f"{e}"
        }, status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes(IsAuthenticated)
def create_product(request: Request) -> Response:
    """
    Method that handles creating a product for a seller
    """
    if not request.user.is_seller:
        return Response({
            "errors": "You are not a seller"
        }, status.HTTP_400_BAD_REQUEST)

    serializer_class = CreateProductSeriallizers(data=request.data)

    if not serializer_class.is_valid():
        return Response(serializer_class.errorss, status.HTTP_400_BAD_REQUEST)

    try:
        # product_name = serializer_class.validated_data.get("name")
        # product_quantity = serializer_class.validated_data.get("quantity")
        product = Products.objects.create(**serializer_class.validated_data, owner=request.user)
        product.save()

        return Response(serializer_class.product_data, status.HTTP_200_OK)

    except Exception as e:
        return Response({
            "errors": str(e)
        }, status.HTTP_400_BAD_REQUEST)

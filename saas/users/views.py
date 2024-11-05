from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializer import CreateCustomUserserializers, CustomUsersLoginSerializer
from drf_yasg.utils import swagger_auto_schema

SWAGGER_TAG_NAME = 'Users'

@swagger_auto_schema(
    method=['POST'],
    request_body=CreateCustomUserserializers,
    responses={
        201: 'Account successfully created',
        400: 'Bad Request',
        500: 'Internal Server Error'
    }
)
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


@swagger_auto_schema(
    method=['POST'],
    request_body=CustomUsersLoginSerializer,
    responses={
        200: 'Successful Login',
        400: 'Bad Request',
        500: 'Internal Server Error'
    }
)
@api_view(['POST'])
def user_login(request: Request) -> Response:
    """
    Post Endpoint for users' login
    """
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


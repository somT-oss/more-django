from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.encoding import smart_bytes, smart_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import CustomUser
from .serializer import CreateCustomUserserializers, CustomUsersLoginSerializer, ForgotPasswordSerializer, ResetPasswordSerializer
from drf_yasg.utils import swagger_auto_schema

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

ENV = os.getenv('ENV')
FULL_DEV_URL = os.getenv('FULL_DEV_URL')

SWAGGER_TAG_NAME = 'Users'

@swagger_auto_schema(
    method='POST',
    request_body=CreateCustomUserserializers,
    responses={
        201: 'Account successfully created',
        400: 'Bad Request',
        500: 'Internal Server Error'
    },
    tags=[SWAGGER_TAG_NAME]
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
    method='POST',
    request_body=CustomUsersLoginSerializer,
    responses={
        200: 'Successful Login',
        400: 'Bad Request',
        500: 'Internal Server Error'
    },
    tags=[SWAGGER_TAG_NAME]
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


@swagger_auto_schema(
    method='POST',
    request_body=ForgotPasswordSerializer,
    responses={
        200: 'Forgot password email sent',
        400: 'Bad request',
    },
    tags=[SWAGGER_TAG_NAME]
)
@api_view(['POST'])
def forgot_password(request: Request) -> Response:
    """
    Forgot password endpoint for users
    """
    serializer_class = ForgotPasswordSerializer(data=request.data)
    if not serializer_class.is_valid():
        return Response(serializer_class.errors, status.HTTP_400_BAD_REQUEST)

    try:
        email = serializer_class.validated_data.get('email')
        user = get_object_or_404(CustomUser, email=email)
        id_base64 = urlsafe_base64_encode(smart_bytes(user.id))
        print(str(id_base64))
        token = PasswordResetTokenGenerator().make_token(user=user)
        endpoint_url = reverse('users:password_token_check_path', kwargs={'id_base64': id_base64, 'token': token})
        site_url = f'{FULL_DEV_URL}{endpoint_url}'

        send_mail(
            subject='Password Reset',
            message=site_url,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.TO_EMAIL, email],
        )
        return Response({
            "message": "Reset password email has been sent to your email"
        }, status.HTTP_200_OK)

    except Exception as e:
        return Response({
            "error": f"{str(e)}"
        }, status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='POST',
    request_body=ResetPasswordSerializer,
    responses={
        200: "Password updated",
        400: "Bad request"
    },
    tags=[SWAGGER_TAG_NAME]
)
@api_view(['POST'])
def reset_password(request: Request) -> Response: 
    serializer_class = ResetPasswordSerializer(data=request.data)

    if not serializer_class.is_valid():
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    
    serializer_class.save()
    return Response({
        "message": "Password updated"
    }, status.HTTP_200_OK)



@swagger_auto_schema(
    method='GET',
    responses={
        200: "Password updated",
        400: "Bad request"
    },
    tags=[SWAGGER_TAG_NAME]
)
@api_view(['GET'])
def password_token_check(request: Request, id_base64: str, token: str) -> Response:
    try:
        user_id = smart_str(urlsafe_base64_decode(id_base64))
        user = get_object_or_404(CustomUser, pk=user_id)

        if not PasswordResetTokenGenerator().check_token(user, token):
            return Response({
                "error": "Invalid token, request a new token"
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "message": "Valid Token",
            "id_base64": id_base64,
            "token": token,
        }, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({
            "error": f"{str(e)}"
        }, status.HTTP_400_BAD_REQUEST)
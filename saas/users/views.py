from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import status
from .serializer import CreateCustomUserserializers

class UserAPIView(APIView):
    """
    User API for creating new users
    """
    def post(self, request: Request) -> Response:
        """
        Post Endpoint for creating users'
        """
        serializer_class = CreateCustomUserserializers(data=request.data)
        if not serializer_class.is_valid():
            return Response(serializer_class.error, status.HTTP_200_OK)

        first_name = serializer_class.validated_data.get("first_name")
        last_name = serializer_class.validated_data.get("last_name")
        serializer_class.save()

        message = {
            "message": f"Account successfully created for {first_name} {last_name}"
        }
        return Response(message, status.HTTP_200_OK)

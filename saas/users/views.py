from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET'])
def view_home(request: Request) -> Response:
    return Response({
        "message": "Hello from user suite"
    }, status.HTTP_200_OK)

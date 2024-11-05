from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from .serializer import CreateProductSeriallizers
from .models import Products


@api_view(['POST'])
@permission_classes([IsAuthenticated])
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
        product = Products.objects.create(**serializer_class.validated_data, owner=request.user)
        product.save()

        return Response(serializer_class.data, status.HTTP_200_OK)

    except Exception as e:
        return Response({
            "errors": str(e)
        }, status.HTTP_400_BAD_REQUEST)

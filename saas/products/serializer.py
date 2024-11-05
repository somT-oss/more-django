from rest_framework import serializers
from .models import Products


class CreateProductSeriallizers(serializers.ModelSerializer):
    name = serializers.CharField(
                            max_length=50,
                            allow_null=False,
                            allow_blank=False,
                            help_text="Product name")
    description = serializers.CharField(
                                   max_length=250,
                                   allow_null=False,
                                   allow_blank=False,
                                   help_text="Product description")
    quantity = serializers.IntegerField(
                                   default=1,
                                   help_text="Quantity of products available")
    price = serializers.CharField(
                                allow_null=False,
                                allow_blank=False,
                                help_text="Price of product"
                                )

    class Meta:
        model = Products
        fields = [
            "name",
            "description",
            "quantity",
            "price"
        ]

from django.contrib import admin
from .models import Products


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    """
    Custom Product Admin panel
    """
    list_display = ("get_owner_first_name", "get_owner_last_name", "get_owner_products")

    def get_owner_first_name(self, obj) -> str:
        """
        Return owner first name
        """
        return obj.owner.first_name

    def get_owner_last_name(self, obj) -> str:
        """
        Return owner last name
        """
        return obj.owner.last_name

    def get_owner_products(self, obj) -> int:
        """
        Returns the number of products a sell has
        @param: obj -> CustomUser object
        """
        number_of_products = Products.objects.filter(owner=obj).count()
        return number_of_products

    get_owner_products.short_description = "number of products"
    get_owner_last_name.short_description = "first_name"
    get_owner_first_name.short_description = "last_name"
